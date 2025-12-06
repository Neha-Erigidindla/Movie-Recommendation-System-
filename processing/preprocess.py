import string
import pickle
import pandas as pd
import ast
import requests
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

# Initialize stemmer and download stopwords
ps = PorterStemmer()
nltk.download('stopwords')

# Cache to avoid repeated poster API calls
poster_cache = {}

# ----------------- Utility Functions -----------------

def get_genres(obj):
    lista = ast.literal_eval(obj)
    return [i['name'] for i in lista]

def get_cast(obj):
    a = ast.literal_eval(obj)
    return [a[i]['name'] for i in range(min(10, len(a)))]

def get_crew(obj):
    l1 = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            l1.append(i['name'])
            break
    return l1

def stemming_stopwords(li):
    ans = [ps.stem(i) for i in li]
    stop_words = set(stopwords.words('english'))
    filtered = [w.lower() for w in ans if w.lower() not in stop_words]
    result = ' '.join([w for w in filtered if len(w) > 2])
    # Remove punctuation
    result = result.translate(str.maketrans('', '', string.punctuation))
    return result

# ----------------- Data Reading & Preprocessing -----------------

def read_csv_to_df():
    # Load CSV files
    credit_ = pd.read_csv(r'Files/tmdb_5000_credits.csv')
    movies = pd.read_csv(r'Files/tmdb_5000_movies.csv')

    # Merge on title
    movies = movies.merge(credit_, on='title')
    movies2 = movies.copy()
    movies2.drop(['homepage', 'tagline'], axis=1, inplace=True)
    movies2 = movies2[['movie_id', 'title', 'budget', 'overview', 'popularity', 
                       'release_date', 'revenue', 'runtime', 'spoken_languages', 
                       'status', 'vote_average', 'vote_count']]

    # Select relevant columns for main processing
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 
                     'cast', 'crew', 'production_companies', 'release_date']]
    movies.dropna(inplace=True)

    # Extract relevant fields
    movies['genres'] = movies['genres'].apply(get_genres)
    movies['keywords'] = movies['keywords'].apply(get_genres)
    movies['top_cast'] = movies['cast'].apply(get_cast)
    movies['director'] = movies['crew'].apply(get_crew)
    movies['prduction_comp'] = movies['production_companies'].apply(get_genres)

    # Clean whitespace
    movies['overview'] = movies['overview'].apply(lambda x: x.split())
    movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['tcast'] = movies['top_cast'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['tcrew'] = movies['director'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['tprduction_comp'] = movies['prduction_comp'].apply(lambda x: [i.replace(" ", "") for i in x])

    # Create combined tags column
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['tcast'] + movies['tcrew']

    # Build final dataframe
    new_df = movies[['movie_id', 'title', 'tags', 'genres', 'keywords', 'tcast', 'tcrew', 'tprduction_comp']]
    new_df['genres'] = new_df['genres'].apply(lambda x: " ".join(x))
    new_df['tcast'] = new_df['tcast'].apply(lambda x: " ".join(x))
    new_df['tprduction_comp'] = new_df['tprduction_comp'].apply(lambda x: " ".join(x))

    new_df['tcast'] = new_df['tcast'].str.lower()
    new_df['genres'] = new_df['genres'].str.lower()
    new_df['tprduction_comp'] = new_df['tprduction_comp'].str.lower()

    # Apply stemming and stopwords removal
    new_df['tags'] = new_df['tags'].apply(stemming_stopwords)
    new_df['keywords'] = new_df['keywords'].apply(stemming_stopwords)

    return movies, new_df, movies2

# ----------------- TMDB API Fetch Functions -----------------

def fetch_posters(movie_id, retries=3, delay=1):
    if movie_id in poster_cache:
        return poster_cache[movie_id]

    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6177b4297dff132d300422e0343471fb'

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                poster_url = "https://image.tmdb.org/t/p/w780/" + poster_path
                poster_cache[movie_id] = poster_url
                return poster_url
            break
        except requests.exceptions.RequestException as e:
            print(f"Error fetching poster for {movie_id}: {e}")
            time.sleep(delay)
            continue

    # Fallback poster
    fallback = "https://media.istockphoto.com/vectors/error-icon-vector-illustration-vector-id922024224?k=6&m=922024224&s=612x612&w=0&h=LXl8Ul7bria6auAXKIjlvb6hRHkAodTqyqBeA6K7R54="
    poster_cache[movie_id] = fallback
    return fallback

def fetch_person_details(id_):
    url = f'https://api.themoviedb.org/3/person/{id_}?api_key=6177b4297dff132d300422e0343471fb'
    try:
        data = requests.get(url, timeout=5).json()
        profile_url = 'https://image.tmdb.org/t/p/w220_and_h330_face' + data.get('profile_path', '')
        biography = data.get('biography', '')
        if not profile_url or profile_url.endswith('None'):
            profile_url = "https://media.istockphoto.com/vectors/error-icon-vector-illustration-vector-id922024224?k=6&m=922024224&s=612x612&w=0&h=LXl8Ul7bria6auAXKIjlvb6hRHkAodTqyqBeA6K7R54="
        return profile_url, biography
    except:
        fallback = "https://media.istockphoto.com/vectors/error-icon-vector-illustration-vector-id922024224?k=6&m=922024224&s=612x612&w=0&h=LXl8Ul7bria6auAXKIjlvb6hRHkAodTqyqBeA6K7R54="
        return fallback, ""

# ----------------- Recommendation Functions -----------------

def recommend(new_df, movie, pickle_file_path):
    with open(pickle_file_path, 'rb') as f:
        similarity_tags = pickle.load(f)

    movie_idx = new_df[new_df['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity_tags[movie_idx])), reverse=True, key=lambda x: x[1])[1:26]

    rec_movie_list = []
    rec_poster_list = []

    for i in movie_list:
        rec_movie_list.append(new_df.iloc[i[0]]['title'])
        rec_poster_list.append(fetch_posters(new_df.iloc[i[0]]['movie_id']))

    return rec_movie_list, rec_poster_list

def vectorise(new_df, col_name):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vec_tags = cv.fit_transform(new_df[col_name]).toarray()
    sim_bt = cosine_similarity(vec_tags)
    return sim_bt

def get_details(selected_movie_name):
    # Load dataframes from pickles
    with open(r'Files/movies_dict.pkl', 'rb') as f:
        movies = pd.DataFrame.from_dict(pickle.load(f))
    with open(r'Files/movies2_dict.pkl', 'rb') as f:
        movies2 = pd.DataFrame.from_dict(pickle.load(f))

    a = movies2[movies2['title'] == selected_movie_name].iloc[0]
    b = movies[movies['title'] == selected_movie_name].iloc[0]

    movie_id = a['movie_id']
    this_poster = fetch_posters(movie_id)
    cast_per = ast.literal_eval(b['cast'])
    cast_id = [i['id'] for i in cast_per]
    available_lang = [l['name'] for l in ast.literal_eval(a['spoken_languages'])]

    info = [
        this_poster, a['budget'], b['genres'], a['overview'], a['release_date'],
        a['revenue'], a['runtime'], available_lang, a['vote_average'], a['vote_count'],
        movie_id, b['cast'], b['director'], available_lang, cast_id
    ]
    return info
