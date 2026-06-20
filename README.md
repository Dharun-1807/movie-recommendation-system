🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using Python and Streamlit.
This project recommends movies based on content similarity using genres, keywords, cast, crew, and overview.

🚀 Live Demo

👉 Add your Streamlit app link here after deployment:

https://movie-recommendation-system-tawegkvzzmym5fk5hdvzs3.streamlit.app/

📌 Project Overview

This system recommends movies similar to a selected movie using Content-Based Filtering.

It analyzes movie features such as:

🎭 Genres
🔑 Keywords
🎬 Cast
🎥 Crew (Director)
📝 Overview

Then it computes similarity between movies using Cosine Similarity.

🧠 Machine Learning Concept
Feature Extraction: Bag of Words (CountVectorizer)
Similarity Measure: Cosine Similarity
Recommendation Type: Content-Based Filtering

🛠️ Tech Stack
Python 🐍
Pandas
NumPy
Scikit-learn
Streamlit

📂 Project Structure
movie-recommendation-system/
│
├── app.py                  # Streamlit web app
├── preprocess.py          # Data preprocessing & model building
├── requirements.txt       # Dependencies
├── tmdb_5000_movies.csv   # Dataset
├── tmdb_5000_credits.csv  # Dataset
├── .gitignore
└── README.md

⚙️ How It Works
Load movie dataset
Merge movie and credits data
Extract important features
Convert text data into vectors
Compute similarity matrix
Recommend top 5 similar movies

▶️ How to Run Locally
1. Clone the repository
git clone https://github.com/Dharun-1807/movie-recommendation-system.git
cd movie-recommendation-system
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the app
streamlit run app.py

📸 Features
🎬 Movie selection dropdown
🤖 AI-powered recommendations
⚡ Fast and lightweight Streamlit UI
📊 Content-based similarity engine

👨‍💻 Author
Dharun Raj
GitHub: Dharun-1807

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!