# 🎬 Movie Recommender System

Welcome to the **Movie Recommender App** — a smart tool that helps users discover movies similar to the ones they already love! This content-based recommendation system suggests films based on metadata like genres, keywords, and storyline.

![Banner](assets/banner.png) <!-- Optional: Replace with your own banner -->

---

## 📌 Features

- 🎥 Select any movie from the dropdown list.
- 🧠 Get top similar movie recommendations using content-based filtering.
- 🖼️ View poster and short plot of each recommended movie via the OMDB API.
- ⚡ Fast, interactive UI built with **Streamlit**.
- 🌐 Static homepage built with HTML, CSS and JavaScript.

---

## 🧰 Tech Stack

| Frontend    | Backend / ML     | External APIs |
|-------------|------------------|---------------|
| HTML, CSS, JS | Python, Streamlit | [OMDB API](https://www.omdbapi.com) |

---

## 🛠️ How It Works

1. **Preprocessing**: Movies metadata is vectorized using **TF-IDF** on features like overview, genre, etc.
2. **Similarity Calculation**: Uses **cosine similarity** to find the most similar titles.
3. **OMDB Integration**: Fetches movie details and posters via OMDB API.

---

## 📁 Project Structure

movie-recommender/
│
├── movierecommendationsystem.ipynb
│
├── streamlit_app/
│ ├── main.py # Streamlit frontend logic
│ ├── recommend.py # Recommendation algorithm
│ ├── omdb_utils.py # OMDB API handler
│ ├── config.json # API keys and settings
│ ├── preprocess.py # TF-IDF & similarity model
│ └── movies.csv # Dataset
│
├── requirements.txt # Python dependencies
├── README.md # Project readme
└── .gitignore


---

## 🔧 Setup Instructions (Local)

1. **Clone the repo**:
   ```bash
   git clone https://github.com/gyan007/movie-recommender.git
   cd movie-recommender/streamlit_app

2. Install dependencies:
   pip install -r requirements.txt

3. Add your OMDB API key:
   Update config.json:
   {
      "OMDB_API_KEY": "your_api_key_here"
   }

4. Run the Streamlit app:
   streamlit run app.py

## 🙋‍♂️ Author
    Gyan Thakur
    [GitHub](https://github.com/gyan007/) ·

