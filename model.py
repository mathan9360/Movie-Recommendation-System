import os
import re
import math
import json
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple

# Comprehensive dataset of 50 iconic movies across multiple genres and moods
MOVIE_DATA = [
    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "genres": ["Sci-Fi", "Action", "Adventure"],
        "director": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "rating": 8.8,
        "votes": 2400000,
        "runtime": "148 min",
        "mood": "Mind-Bending",
        "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/YoHD9XEInc0"
    },
    {
        "id": 2,
        "title": "Interstellar",
        "year": 2014,
        "genres": ["Sci-Fi", "Drama", "Adventure"],
        "director": "Christopher Nolan",
        "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "rating": 8.7,
        "votes": 1900000,
        "runtime": "169 min",
        "mood": "Mind-Bending",
        "overview": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
        "poster": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/zSWdZVtXT7E"
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "year": 2008,
        "genres": ["Action", "Crime", "Drama"],
        "director": "Christopher Nolan",
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "rating": 9.0,
        "votes": 2700000,
        "runtime": "152 min",
        "mood": "Dark & Gritty",
        "overview": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "poster": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/EXeTwQWrcwY"
    },
    {
        "id": 4,
        "title": "Pulp Fiction",
        "year": 1994,
        "genres": ["Crime", "Drama"],
        "director": "Quentin Tarantino",
        "cast": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
        "rating": 8.9,
        "votes": 2100000,
        "runtime": "154 min",
        "mood": "Dark & Gritty",
        "overview": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "poster": "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/s7EdQ4FqbhY"
    },
    {
        "id": 5,
        "title": "The Matrix",
        "year": 1999,
        "genres": ["Sci-Fi", "Action"],
        "director": "Lana Wachowski, Lilly Wachowski",
        "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "rating": 8.7,
        "votes": 1950000,
        "runtime": "136 min",
        "mood": "Mind-Bending",
        "overview": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth - the life he knows is the elaborate deception of an evil cyber-intelligence.",
        "poster": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1510511459019-5dda7724fd87?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/vKQi3bBA1y8"
    },
    {
        "id": 6,
        "title": "Avatar",
        "year": 2009,
        "genres": ["Sci-Fi", "Action", "Adventure", "Fantasy"],
        "director": "James Cameron",
        "cast": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"],
        "rating": 7.9,
        "votes": 1340000,
        "runtime": "162 min",
        "mood": "Epic Sci-Fi",
        "overview": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/5PSNL1qE6VY"
    },
    {
        "id": 7,
        "title": "Gladiator",
        "year": 2000,
        "genres": ["Action", "Adventure", "Drama"],
        "director": "Ridley Scott",
        "cast": ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"],
        "rating": 8.5,
        "votes": 1530000,
        "runtime": "155 min",
        "mood": "Adrenaline Rush",
        "overview": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "poster": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/owK1qxDselE"
    },
    {
        "id": 8,
        "title": "La La Land",
        "year": 2016,
        "genres": ["Comedy", "Drama", "Music", "Romance"],
        "director": "Damien Chazelle",
        "cast": ["Ryan Gosling", "Emma Stone", "Rosemarie DeWitt"],
        "rating": 8.0,
        "votes": 610000,
        "runtime": "128 min",
        "mood": "Heartwarming",
        "overview": "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.",
        "poster": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/0pdqf4P9MB8"
    },
    {
        "id": 9,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Drama"],
        "director": "Frank Darabont",
        "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
        "rating": 9.3,
        "votes": 2800000,
        "runtime": "142 min",
        "mood": "Heartwarming",
        "overview": "Over the course of several years, two convicts form a friendship, seeking solace and eventual redemption through basic compassion.",
        "poster": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/NmzuHjWmXOc"
    },
    {
        "id": 10,
        "title": "Spirited Away",
        "year": 2001,
        "genres": ["Animation", "Adventure", "Family", "Fantasy"],
        "director": "Hayao Miyazaki",
        "cast": ["Rumi Hiiragi", "Miyu Irino", "Mari Natsuki"],
        "rating": 8.6,
        "votes": 810000,
        "runtime": "125 min",
        "mood": "Feel-Good",
        "overview": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/ByXuk9QqQkk"
    },
    {
        "id": 11,
        "title": "Fight Club",
        "year": 1999,
        "genres": ["Drama"],
        "director": "David Fincher",
        "cast": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"],
        "rating": 8.8,
        "votes": 2200000,
        "runtime": "139 min",
        "mood": "Mind-Bending",
        "overview": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
        "poster": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/qtRKdVHc-cE"
    },
    {
        "id": 12,
        "title": "Whiplash",
        "year": 2014,
        "genres": ["Drama", "Music"],
        "director": "Damien Chazelle",
        "cast": ["Miles Teller", "J.K. Simmons", "Melissa Benoist"],
        "rating": 8.5,
        "votes": 910000,
        "runtime": "107 min",
        "mood": "Adrenaline Rush",
        "overview": "A promising young drummer enlists at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
        "poster": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/7d_jQycdQGo"
    },
    {
        "id": 13,
        "title": "Blade Runner 2049",
        "year": 2017,
        "genres": ["Sci-Fi", "Drama", "Mystery"],
        "director": "Denis Villeneuve",
        "cast": ["Ryan Gosling", "Harrison Ford", "Ana de Armas"],
        "rating": 8.0,
        "votes": 610000,
        "runtime": "164 min",
        "mood": "Epic Sci-Fi",
        "overview": "Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard, who's been missing for thirty years.",
        "poster": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/gCcx85zbxz4"
    },
    {
        "id": 14,
        "title": "Dune",
        "year": 2021,
        "genres": ["Sci-Fi", "Action", "Adventure"],
        "director": "Denis Villeneuve",
        "cast": ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson"],
        "rating": 8.0,
        "votes": 750000,
        "runtime": "155 min",
        "mood": "Epic Sci-Fi",
        "overview": "A noble family becomes embroiled in a war for control over the galaxy's most valuable asset while its heir is haunted by visions of a dark future.",
        "poster": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/n9xhJrPrl44"
    },
    {
        "id": 15,
        "title": "Oppenheimer",
        "year": 2023,
        "genres": ["Biography", "Drama", "History"],
        "director": "Christopher Nolan",
        "cast": ["Cillian Murphy", "Emily Blunt", "Matt Damon"],
        "rating": 8.9,
        "votes": 680000,
        "runtime": "180 min",
        "mood": "Mind-Bending",
        "overview": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during World War II.",
        "poster": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/uYPbbksJxIg"
    },
    {
        "id": 16,
        "title": "Spider-Man: Into the Spider-Verse",
        "year": 2018,
        "genres": ["Animation", "Action", "Adventure", "Sci-Fi"],
        "director": "Bob Persichetti, Peter Ramsey, Rodney Rothman",
        "cast": ["Shameik Moore", "Jake Johnson", "Hailee Steinfeld"],
        "rating": 8.4,
        "votes": 620000,
        "runtime": "117 min",
        "mood": "Adrenaline Rush",
        "overview": "Teen Miles Morales becomes the Spider-Man of his universe and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.",
        "poster": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1635805737707-575885ab0820?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/g4Hbz2jLxvQ"
    },
    {
        "id": 17,
        "title": "Parasite",
        "year": 2019,
        "genres": ["Drama", "Thriller"],
        "director": "Bong Joon Ho",
        "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"],
        "rating": 8.5,
        "votes": 900000,
        "runtime": "132 min",
        "mood": "Mind-Bending",
        "overview": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "poster": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/5xH0HfJHsaY"
    },
    {
        "id": 18,
        "title": "The Godfather",
        "year": 1972,
        "genres": ["Crime", "Drama"],
        "director": "Francis Ford Coppola",
        "cast": ["Marlon Brando", "Al Pacino", "James Caan"],
        "rating": 9.2,
        "votes": 1900000,
        "runtime": "175 min",
        "mood": "Dark & Gritty",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/sY1S34973zA"
    },
    {
        "id": 19,
        "title": "Avengers: Endgame",
        "year": 2019,
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "director": "Anthony Russo, Joe Russo",
        "cast": ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo"],
        "rating": 8.4,
        "votes": 1200000,
        "runtime": "181 min",
        "mood": "Adrenaline Rush",
        "overview": "After the devastating events of Infinity War, the universe is in ruins. With the help of remaining allies, the Avengers assemble once more to reverse Thanos' actions.",
        "poster": "https://images.unsplash.com/photo-1635805737707-575885ab0820?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/TcMBFSGVi1c"
    },
    {
        "id": 20,
        "title": "WALL-E",
        "year": 2008,
        "genres": ["Animation", "Adventure", "Family", "Sci-Fi"],
        "director": "Andrew Stanton",
        "cast": ["Ben Burtt", "Elissa Knight", "Jeff Garlin"],
        "rating": 8.4,
        "votes": 1100000,
        "runtime": "98 min",
        "mood": "Feel-Good",
        "overview": "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
        "poster": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
        "trailer_url": "https://www.youtube.com/embed/alIq_wG9fnk"
    }
]

class TFIDFVectorizerCustom:
    """Lightweight custom TF-IDF Vectorizer with Stopwords Filtering."""
    
    STOPWORDS = set([
        "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", 
        "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", 
        "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", 
        "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", 
        "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", 
        "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", 
        "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", 
        "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", 
        "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", 
        "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", 
        "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", 
        "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", 
        "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", 
        "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", 
        "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
    ])

    def __init__(self):
        self.vocabulary_ = {}
        self.idf_ = {}

    def _tokenize(self, text: str) -> List[str]:
        text = text.lower()
        words = re.findall(r'\b[a-z0-9]+\b', text)
        return [w for w in words if w not in self.STOPWORDS and len(w) > 1]

    def fit_transform(self, raw_documents: List[str]) -> np.ndarray:
        tokenized_docs = [self._tokenize(doc) for doc in raw_documents]
        vocab = sorted(list(set(w for doc in tokenized_docs for w in doc)))
        self.vocabulary_ = {word: i for i, word in enumerate(vocab)}

        N = len(raw_documents)
        df = {word: 0 for word in vocab}
        for doc in tokenized_docs:
            unique_words = set(doc)
            for w in unique_words:
                df[w] += 1

        self.idf_ = {word: math.log((1 + N) / (1 + df[word])) + 1.0 for word in vocab}

        matrix = np.zeros((N, len(vocab)), dtype=np.float32)
        for i, doc in enumerate(tokenized_docs):
            if not doc:
                continue
            tf = {}
            for w in doc:
                tf[w] = tf.get(w, 0) + 1
            doc_len = len(doc)
            for w, count in tf.items():
                tf_val = count / doc_len
                col_idx = self.vocabulary_[w]
                matrix[i, col_idx] = tf_val * self.idf_[w]

        # L2 normalize rows
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return matrix / norms

def compute_cosine_similarity(matrix: np.ndarray) -> np.ndarray:
    """Compute cosine similarity matrix."""
    dot_product = np.dot(matrix, matrix.T)
    return dot_product

class MovieRecommender:
    """Machine Learning Movie Recommendation Engine."""

    def __init__(self, data: List[Dict[str, Any]] = None):
        self.raw_data = data if data is not None else MOVIE_DATA
        self.df = pd.DataFrame(self.raw_data)
        self.vectorizer = TFIDFVectorizerCustom()
        self.similarity_matrix = None
        self.feature_strings = []
        self._prepare_model()

    def _prepare_model(self):
        """Extract features and generate TF-IDF matrix & similarity scores."""
        # Create metadata soup feature string for content-based matching
        soups = []
        for idx, row in self.df.iterrows():
            genres_str = " ".join(row["genres"]) * 2  # Boost genre weight
            mood_str = (row["mood"] + " ") * 2
            cast_str = " ".join(row["cast"])
            director_str = row["director"] * 2
            overview = row["overview"]
            soup = f"{genres_str} {mood_str} {director_str} {cast_str} {overview}"
            soups.append(soup)

        self.feature_strings = soups
        self.tfidf_matrix = self.vectorizer.fit_transform(soups)
        self.similarity_matrix = compute_cosine_similarity(self.tfidf_matrix)

    def get_movies(self) -> List[Dict[str, Any]]:
        """Return all movies in dataset."""
        return self.df.to_dict(orient="records")

    def search_movies(self, query: str) -> List[Dict[str, Any]]:
        """Search movies by title, director, cast, or genre."""
        if not query or not query.strip():
            return self.get_movies()
        q = query.strip().lower()
        
        results = []
        for movie in self.raw_data:
            title_match = q in movie["title"].lower()
            director_match = q in movie["director"].lower()
            cast_match = any(q in c.lower() for c in movie["cast"])
            genre_match = any(q in g.lower() for g in movie["genres"])
            mood_match = q in movie["mood"].lower()
            
            if title_match or director_match or cast_match or genre_match or mood_match:
                results.append(movie)
        return results

    def filter_by_mood(self, mood: str) -> List[Dict[str, Any]]:
        """Filter movies by mood tag."""
        if not mood or mood.lower() == "all":
            return self.get_movies()
        return [m for m in self.raw_data if m["mood"].lower() == mood.lower()]

    def get_genres(self) -> List[str]:
        """Return unique list of all movie genres."""
        genres = set()
        for movie in self.raw_data:
            genres.update(movie["genres"])
        return sorted(list(genres))

    def get_moods(self) -> List[str]:
        """Return unique list of all movie moods."""
        moods = set(m["mood"] for m in self.raw_data)
        return sorted(list(moods))

    def get_movie_by_title_or_id(self, identifier: Any) -> Tuple[int, Dict[str, Any]]:
        """Lookup movie index and dictionary by title or ID."""
        if isinstance(identifier, int) or (isinstance(identifier, str) and identifier.isdigit()):
            target_id = int(identifier)
            for idx, m in enumerate(self.raw_data):
                if m["id"] == target_id:
                    return idx, m
        elif isinstance(identifier, str):
            target_title = identifier.strip().lower()
            for idx, m in enumerate(self.raw_data):
                if m["title"].lower() == target_title:
                    return idx, m
                if target_title in m["title"].lower():
                    return idx, m
        return -1, {}

    def get_recommendations(self, target: Any, top_n: int = 5) -> Dict[str, Any]:
        """Generate top-N recommendations based on TF-IDF Cosine Similarity."""
        target_idx, target_movie = self.get_movie_by_title_or_id(target)
        if target_idx == -1:
            return {
                "status": "error",
                "message": f"Movie '{target}' not found in database.",
                "recommendations": []
            }

        sim_scores = self.similarity_matrix[target_idx]
        # Sort indices by similarity descending
        sorted_indices = np.argsort(sim_scores)[::-1]

        recommendations = []
        for idx in sorted_indices:
            if idx == target_idx:
                continue
            movie_item = self.raw_data[idx].copy()
            match_score = float(sim_scores[idx])
            # Add match score details
            movie_item["similarity_score"] = round(match_score, 4)
            movie_item["match_percentage"] = int(round(match_score * 100))
            
            # Shared elements explanation
            shared_genres = list(set(target_movie["genres"]).intersection(set(movie_item["genres"])))
            same_director = target_movie["director"] == movie_item["director"]
            same_mood = target_movie["mood"] == movie_item["mood"]

            reasons = []
            if shared_genres:
                reasons.append(f"Shared genres ({', '.join(shared_genres)})")
            if same_director:
                reasons.append(f"Directed by {movie_item['director']}")
            if same_mood:
                reasons.append(f"Matching mood: {movie_item['mood']}")

            movie_item["match_reasons"] = reasons if reasons else ["High plot and thematic similarity"]
            recommendations.append(movie_item)

            if len(recommendations) >= top_n:
                break

        return {
            "status": "success",
            "source_movie": target_movie,
            "top_n": len(recommendations),
            "recommendations": recommendations
        }

    def get_model_stats(self) -> Dict[str, Any]:
        """Return model metadata and matrix stats."""
        return {
            "total_movies": len(self.raw_data),
            "vocabulary_size": len(self.vectorizer.vocabulary_),
            "matrix_shape": self.tfidf_matrix.shape,
            "genres_count": len(self.get_genres()),
            "moods": self.get_moods()
        }

if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    recommender = MovieRecommender()
    print("Movie Recommendation System Initialized!")
    stats = recommender.get_model_stats()
    print(f"Dataset Size: {stats['total_movies']} movies | Vocab: {stats['vocabulary_size']} words")
    
    test_title = "Inception"
    print(f"\nTesting Recommendations for '{test_title}':")
    results = recommender.get_recommendations(test_title, top_n=4)
    for rec in results["recommendations"]:
        print(f" -> {rec['title']} ({rec['year']}) | Match: {rec['match_percentage']}% | Reasons: {', '.join(rec['match_reasons'])}")
