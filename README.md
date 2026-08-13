# 🎬 CineMind AI — Movie Recommendation System & Super Web Application

[![Python 3.11](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org)
[![CSS3](https://img.shields.io/badge/CSS3-Vanilla-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A state-of-the-art **Machine Learning Movie Recommendation Engine** (`model.py`) powered by **TF-IDF Vectorization** and **Cosine Similarity Matrix** algorithms, paired with a stunning dark-mode cinematic **Super Web Application** interface.

---

## ✨ Highlights & Features

- 🧠 **TF-IDF Content-Based Vector Engine**: Vectorizes movie metadata (Genres, Plot Overview, Mood Tags, Directors, Cast) to measure exact high-dimensional similarity.
- 🎨 **Cinematic Glassmorphism UI**: High-end dark theme (`#090c10`) with frosted glass navigation, glowing neon cyan/violet accents, 3D card hover elevation, and fluid responsive design.
- 🎬 **Hero Spotlight**: Dynamic featured movie hero banner with IMDb ratings, runtimes, mood badges, and direct trailer launcher.
- 🎛️ **AI Recommendation Studio**: Customize base target movies and fine-tune top-$N$ recommendation counts with real-time score calculation.
- 🧭 **Mood Explorer**: Instant category filters including *Mind-Bending*, *Adrenaline Rush*, *Dark & Gritty*, *Feel-Good*, *Epic Sci-Fi*, and *Heartwarming*.
- 🍿 **Interactive Trailer & Detail Modal**: Fullscreen YouTube trailer video embeds, complete cast/crew breakdowns, and similarity match reasoning.
- 📊 **Model Analytics Dashboard**: Live metrics inspector displaying dataset counts, vector matrix shapes, and vocabulary size.
- ⚡ **Dual Execution Engine**: Runs seamless client-side similarity calculations in any browser offline OR integrates with the Python REST API server.

---

## 📁 Repository Structure

```text
movies_recomented_project/
├── model.py            # Core ML Recommender Class (TF-IDF & Cosine Similarity)
├── server.py           # Python HTTP REST API Server & static file host
├── test_model.py       # Automated verification test suite
├── index.html          # Super Web Application HTML5 markup
├── styles.css          # Modern dark-mode Glassmorphic stylesheet
├── app.js              # Application frontend controller & client ML engine
└── README.md           # Project documentation
```

---

## 🚀 Quick Start Guide

### Option 1: Run with Python REST API Server (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mathan9360/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
   ```

2. **Run the backend server:**
   ```bash
   python server.py
   ```

3. **Open in browser:**
   Navigate to `http://localhost:8000`

---

### Option 2: Run Unit Verification Tests

To verify the TF-IDF matrix generation and cosine similarity calculation:
```bash
python test_model.py
```

Expected output:
```text
--------------------------------------------------
Running Automated Verification Tests for model.py
--------------------------------------------------
[OK] Model stats verified: 20 movies, matrix shape (20, 473)
[OK] 'Inception' Recommendations: ['Interstellar', 'Oppenheimer', 'Dune']
[OK] 'Nolan' Search matched 4 movies
[OK] Mood filter 'Mind-Bending' matched 6 movies

[SUCCESS] ALL TESTS PASSED!
```

---

## 📡 REST API Documentation

The `server.py` exposes the following HTTP JSON endpoints:

| Endpoint | Method | Description | Example Query |
| :--- | :--- | :--- | :--- |
| `/api/movies` | `GET` | Get all indexed movies & genres | `http://localhost:8000/api/movies` |
| `/api/recommend` | `GET` | Get TF-IDF top-N recommendations | `http://localhost:8000/api/recommend?title=Inception&top_n=6` |
| `/api/search` | `GET` | Live search by title, director, or cast | `http://localhost:8000/api/search?q=Nolan` |
| `/api/mood` | `GET` | Filter catalog by mood tag | `http://localhost:8000/api/mood?mood=Mind-Bending` |
| `/api/stats` | `GET` | Return model vocabulary & matrix stats | `http://localhost:8000/api/stats` |

---

## 🧮 Mathematical Architecture

The similarity score between a target movie vector $A$ and a catalog movie vector $B$ is derived using the Cosine Similarity formula:

$$\text{Similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$

Where features $A_i$ are weighted using Term Frequency-Inverse Document Frequency (TF-IDF):

$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

---

## 📜 License
Distributed under the MIT License. Developed for Movie Recommendation Systems.
