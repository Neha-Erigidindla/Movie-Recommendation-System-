# 🎬 Movie Recommender System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![NLP](https://img.shields.io/badge/NLP-Enabled-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Unlock Your Next Favorite Film!**

*An intelligent NLP-powered recommendation engine that helps you discover movies tailored to your preferences*

[🚀 Try Live Demo](https://your-app-link.streamlit.app) | [📖 HLD](./HLD.md) | [📖 LLD](./LLD.md) | [🐛 Report Bug](https://github.com/Neha-Erigidindla/Movie-Recommendation-System-/issues)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Installation Guide](#-installation-guide)
- [Usage](#-usage)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

Our Movie Recommender System leverages **Natural Language Processing (NLP)** and the **Bag-of-Words** model to deliver personalized movie recommendations. By analyzing similarities in cast, genres, tags, and production companies, the system helps you discover films that match your taste.

Built with Python and deployed on Streamlit, this application offers an intuitive interface for exploring movie recommendations, viewing detailed descriptions, and browsing through an extensive movie catalog.

**Key Highlights:**
- Content-based filtering using NLP techniques
- Cosine similarity for recommendation matching
- Real-time movie suggestions
- Comprehensive movie database with 5000+ movies
- Interactive and responsive UI

---

## ✨ Features

- 🎭 **Smart Recommendations** - Get personalized suggestions based on multiple factors
- 🔍 **Content-Based Filtering** - Utilizes cast, genres, tags, and production companies
- 📊 **Movie Details** - Access comprehensive information about each film
- 👥 **Cast Information** - Explore detailed cast profiles
- 📚 **Complete Movie Catalog** - Browse through the entire movie database
- 🎨 **User-Friendly Interface** - Clean and intuitive Streamlit design
- ⚡ **Fast Performance** - Optimized recommendation engine using pre-computed similarity matrix
- 📱 **Responsive Design** - Works seamlessly across devices

---

## 🎥 Demo

### Try the Live Application

Visit our deployed application: **[Movie Recommender System App](https://your-app-link.streamlit.app)**

### Screenshots

<!-- Add your screenshots here -->
![Home Page](screenshots/home.png)
![Recommendations](screenshots/recommendations.png)
![Movie Details](screenshots/details.png)

---

## 📥 Installation Guide

Follow these steps to set up the application locally:

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Step-by-Step Installation

1. **Clone the Repository**

```bash
git clone https://github.com/Neha-Erigidindla/Movie-Recommendation-System-.git
cd Movie-Recommendation-System-
```

2. **Create a Virtual Environment** (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Download Required Data Files**

Make sure you have the following files in your project directory:
- `movies.csv` - Movie dataset
- `credits.csv` - Cast and crew information
- Or run the preprocessing notebook to generate `similarity.pkl` and `movie_dict.pkl`

5. **Run the Application**

```bash
streamlit run main.py
```

6. **Access the App**

The application will automatically open in your default browser at `http://localhost:8501`

> **Note**: On first run, the application may take a few moments to initialize and create necessary files (similarity matrix and movie dictionary). This is a one-time process.

---

## 🎮 Usage

1. **Launch the Application** - Start the Streamlit app using the command above
2. **Select a Movie** - Choose a movie from the dropdown menu (5000+ movies available)
3. **Get Recommendations** - Click the "Show Recommendations" button to see similar movies
4. **View Details** - Click on any recommended movie to view its description, rating, and cast
5. **Browse Catalog** - Use the sidebar to explore the complete movie list by genre, year, or rating

### Example Workflow

```python
# User selects "The Dark Knight"
# System analyzes:
# - Genre: Action, Crime, Drama
# - Cast: Christian Bale, Heath Ledger, Aaron Eckhart
# - Director: Christopher Nolan
# - Tags: dc comics, crime, superhero

# Returns similar movies:
# 1. Batman Begins
# 2. The Dark Knight Rises
# 3. Inception
# 4. The Prestige
# 5. Interstellar
```

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.8+ |
| **Streamlit** | Web application framework | 1.28+ |
| **Pandas** | Data manipulation and analysis | 2.0+ |
| **NumPy** | Numerical computations | 1.24+ |
| **Scikit-learn** | Machine learning and NLP | 1.3+ |
| **NLTK** | Natural language processing | 3.8+ |
| **Pickle** | Model serialization | Built-in |
| **Requests** | API calls (TMDB) | 2.31+ |

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── main.py                          # Main Streamlit application
├── requirements.txt                 # Project dependencies
├── README.md                        # Project documentation
├── HLD.md                          # High-Level Design document
├── LLD.md                          # Low-Level Design document
│
├── data/                           # Dataset folder
│   ├── movies.csv                  # Movie metadata
│   ├── credits.csv                 # Cast and crew data
│   └── tmdb_5000_movies.csv        # TMDB dataset (alternative)
│
├── models/                         # Saved models and files
│   ├── similarity.pkl              # Pre-computed similarity matrix
│   └── movie_dict.pkl              # Processed movie dictionary
│
├── notebooks/                      # Jupyter notebooks for development
│   ├── data_preprocessing.ipynb    # Data cleaning and preparation
│   └── model_building.ipynb        # Model training and testing
│
├── src/                            # Source code modules
│   ├── __init__.py
│   ├── preprocessor.py             # Data preprocessing functions
│   ├── recommender.py              # Recommendation engine
│   └── utils.py                    # Utility functions
│
├── screenshots/                    # Application screenshots
│   ├── home.png
│   ├── recommendations.png
│   └── details.png
│
└── tests/                          # Unit tests
    ├── test_preprocessor.py
    └── test_recommender.py
```

---

## 🏗️ Architecture

### High-Level Architecture

```
User Interface (Streamlit)
         ↓
Recommendation Engine
         ↓
    [Processing Layer]
         ↓
[Similarity Computation]
         ↓
    Movie Database
```

For detailed architecture, please refer to:
- **[High-Level Design (HLD)](./HLD.md)** - System architecture, components, and data flow
- **[Low-Level Design (LLD)](./LLD.md)** - Detailed implementation, algorithms, and code structure

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src
```

---

## 🚀 Deployment

The application is deployed on Streamlit Cloud. To deploy your own version:

1. Fork this repository
2. Sign up on [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy with one click

For other deployment options (Heroku, AWS, Docker), see [Deployment Guide](docs/deployment.md)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

---

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Movie data sourced from [TMDB API](https://www.themoviedb.org/documentation/api)
- Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Inspired by content-based filtering techniques from research papers
- Built with ❤️ using Streamlit framework
- Special thanks to the open-source community

---

## 📊 Project Stats

- **Stars**: Give this project a ⭐ if you found it helpful!
- **Forks**: Feel free to fork and customize
- **Issues**: Report bugs or request features
- **Pull Requests**: Contributions are welcome

---

## 👤 Contact

**Neha Erigidindla**

- GitHub: [@Neha-Erigidindla](https://github.com/Neha-Erigidindla)
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- Project Link: [Movie Recommendation System](https://github.com/Neha-Erigidindla/Movie-Recommendation-System-)

---

## 🎓 Learning Resources

If you want to learn more about recommendation systems and NLP:

- [Recommendation Systems Tutorial](https://www.coursera.org/learn/recommender-systems)
- [Natural Language Processing with Python](https://www.nltk.org/book/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Neha Erigidindla

</div>
