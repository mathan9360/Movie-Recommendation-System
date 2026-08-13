/* ==========================================================================
   CineMind AI — Application Frontend Controller & Client Engine
   ========================================================================== */

// Client Dataset Fallback (Mirrors model.py)
const FALLBACK_MOVIES = [
  {
    id: 1,
    title: "Inception",
    year: 2010,
    genres: ["Sci-Fi", "Action", "Adventure"],
    director: "Christopher Nolan",
    cast: ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
    rating: 8.8,
    votes: 2400000,
    runtime: "148 min",
    mood: "Mind-Bending",
    overview: "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
    poster: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/YoHD9XEInc0"
  },
  {
    id: 2,
    title: "Interstellar",
    year: 2014,
    genres: ["Sci-Fi", "Drama", "Adventure"],
    director: "Christopher Nolan",
    cast: ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
    rating: 8.7,
    votes: 1900000,
    runtime: "169 min",
    mood: "Mind-Bending",
    overview: "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot is tasked to pilot a spacecraft to find a new home for mankind.",
    poster: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/zSWdZVtXT7E"
  },
  {
    id: 3,
    title: "The Dark Knight",
    year: 2008,
    genres: ["Action", "Crime", "Drama"],
    director: "Christopher Nolan",
    cast: ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
    rating: 9.0,
    votes: 2700000,
    runtime: "152 min",
    mood: "Dark & Gritty",
    overview: "When the menace known as the Joker wreaks havoc on Gotham, Batman must accept one of the greatest psychological tests of his ability to fight injustice.",
    poster: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/EXeTwQWrcwY"
  },
  {
    id: 4,
    title: "Pulp Fiction",
    year: 1994,
    genres: ["Crime", "Drama"],
    director: "Quentin Tarantino",
    cast: ["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
    rating: 8.9,
    votes: 2100000,
    runtime: "154 min",
    mood: "Dark & Gritty",
    overview: "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    poster: "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/s7EdQ4FqbhY"
  },
  {
    id: 5,
    title: "The Matrix",
    year: 1999,
    genres: ["Sci-Fi", "Action"],
    director: "Lana Wachowski, Lilly Wachowski",
    cast: ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
    rating: 8.7,
    votes: 1950000,
    runtime: "136 min",
    mood: "Mind-Bending",
    overview: "When a computer hacker learns from mysterious rebels about the true nature of his reality, he joins the war against its controllers.",
    poster: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1510511459019-5dda7724fd87?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/vKQi3bBA1y8"
  },
  {
    id: 6,
    title: "Avatar",
    year: 2009,
    genres: ["Sci-Fi", "Action", "Adventure", "Fantasy"],
    director: "James Cameron",
    cast: ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"],
    rating: 7.9,
    votes: 1340000,
    runtime: "162 min",
    mood: "Epic Sci-Fi",
    overview: "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the alien world.",
    poster: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/5PSNL1qE6VY"
  },
  {
    id: 7,
    title: "Gladiator",
    year: 2000,
    genres: ["Action", "Adventure", "Drama"],
    director: "Ridley Scott",
    cast: ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"],
    rating: 8.5,
    votes: 1530000,
    runtime: "155 min",
    mood: "Adrenaline Rush",
    overview: "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
    poster: "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/owK1qxDselE"
  },
  {
    id: 8,
    title: "La La Land",
    year: 2016,
    genres: ["Comedy", "Drama", "Music", "Romance"],
    director: "Damien Chazelle",
    cast: ["Ryan Gosling", "Emma Stone", "Rosemarie DeWitt"],
    rating: 8.0,
    votes: 610000,
    runtime: "128 min",
    mood: "Heartwarming",
    overview: "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.",
    poster: "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/0pdqf4P9MB8"
  },
  {
    id: 9,
    title: "The Shawshank Redemption",
    year: 1994,
    genres: ["Drama"],
    director: "Frank Darabont",
    cast: ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
    rating: 9.3,
    votes: 2800000,
    runtime: "142 min",
    mood: "Heartwarming",
    overview: "Over the course of several years, two convicts form a friendship, seeking solace and eventual redemption through basic compassion.",
    poster: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/NmzuHjWmXOc"
  },
  {
    id: 10,
    title: "Spirited Away",
    year: 2001,
    genres: ["Animation", "Adventure", "Family", "Fantasy"],
    director: "Hayao Miyazaki",
    cast: ["Rumi Hiiragi", "Miyu Irino", "Mari Natsuki"],
    rating: 8.6,
    votes: 810000,
    runtime: "125 min",
    mood: "Feel-Good",
    overview: "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits.",
    poster: "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/ByXuk9QqQkk"
  },
  {
    id: 11,
    title: "Fight Club",
    year: 1999,
    genres: ["Drama"],
    director: "David Fincher",
    cast: ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"],
    rating: 8.8,
    votes: 2200000,
    runtime: "139 min",
    mood: "Mind-Bending",
    overview: "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
    poster: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/qtRKdVHc-cE"
  },
  {
    id: 12,
    title: "Whiplash",
    year: 2014,
    genres: ["Drama", "Music"],
    director: "Damien Chazelle",
    cast: ["Miles Teller", "J.K. Simmons", "Melissa Benoist"],
    rating: 8.5,
    votes: 910000,
    runtime: "107 min",
    mood: "Adrenaline Rush",
    overview: "A promising young drummer enlists at a cut-throat music conservatory where his dreams of greatness are mentored by an unyielding instructor.",
    poster: "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/7d_jQycdQGo"
  },
  {
    id: 13,
    title: "Blade Runner 2049",
    year: 2017,
    genres: ["Sci-Fi", "Drama", "Mystery"],
    director: "Denis Villeneuve",
    cast: ["Ryan Gosling", "Harrison Ford", "Ana de Armas"],
    rating: 8.0,
    votes: 610000,
    runtime: "164 min",
    mood: "Epic Sci-Fi",
    overview: "Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard, who's been missing for thirty years.",
    poster: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/gCcx85zbxz4"
  },
  {
    id: 14,
    title: "Dune",
    year: 2021,
    genres: ["Sci-Fi", "Action", "Adventure"],
    director: "Denis Villeneuve",
    cast: ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson"],
    rating: 8.0,
    votes: 750000,
    runtime: "155 min",
    mood: "Epic Sci-Fi",
    overview: "A noble family becomes embroiled in a war for control over the galaxy's most valuable asset while its heir is haunted by visions of a dark future.",
    poster: "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/n9xhJrPrl44"
  },
  {
    id: 15,
    title: "Oppenheimer",
    year: 2023,
    genres: ["Biography", "Drama", "History"],
    director: "Christopher Nolan",
    cast: ["Cillian Murphy", "Emily Blunt", "Matt Damon"],
    rating: 8.9,
    votes: 680000,
    runtime: "180 min",
    mood: "Mind-Bending",
    overview: "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during World War II.",
    poster: "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/uYPbbksJxIg"
  },
  {
    id: 16,
    title: "Spider-Man: Into the Spider-Verse",
    year: 2018,
    genres: ["Animation", "Action", "Adventure", "Sci-Fi"],
    director: "Bob Persichetti, Peter Ramsey, Rodney Rothman",
    cast: ["Shameik Moore", "Jake Johnson", "Hailee Steinfeld"],
    rating: 8.4,
    votes: 620000,
    runtime: "117 min",
    mood: "Adrenaline Rush",
    overview: "Teen Miles Morales becomes the Spider-Man of his universe and must join with five spider-powered individuals from other dimensions to stop a threat.",
    poster: "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1635805737707-575885ab0820?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/g4Hbz2jLxvQ"
  },
  {
    id: 17,
    title: "Parasite",
    year: 2019,
    genres: ["Drama", "Thriller"],
    director: "Bong Joon Ho",
    cast: ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"],
    rating: 8.5,
    votes: 900000,
    runtime: "132 min",
    mood: "Mind-Bending",
    overview: "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
    poster: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/5xH0HfJHsaY"
  },
  {
    id: 18,
    title: "The Godfather",
    year: 1972,
    genres: ["Crime", "Drama"],
    director: "Francis Ford Coppola",
    cast: ["Marlon Brando", "Al Pacino", "James Caan"],
    rating: 9.2,
    votes: 1900000,
    runtime: "175 min",
    mood: "Dark & Gritty",
    overview: "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    poster: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/sY1S34973zA"
  },
  {
    id: 19,
    title: "Avengers: Endgame",
    year: 2019,
    genres: ["Action", "Adventure", "Sci-Fi"],
    director: "Anthony Russo, Joe Russo",
    cast: ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo"],
    rating: 8.4,
    votes: 1200000,
    runtime: "181 min",
    mood: "Adrenaline Rush",
    overview: "After the devastating events of Infinity War, the universe is in ruins. With the help of remaining allies, the Avengers assemble once more.",
    poster: "https://images.unsplash.com/photo-1635805737707-575885ab0820?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/TcMBFSGVi1c"
  },
  {
    id: 20,
    title: "WALL-E",
    year: 2008,
    genres: ["Animation", "Adventure", "Family", "Sci-Fi"],
    director: "Andrew Stanton",
    cast: ["Ben Burtt", "Elissa Knight", "Jeff Garlin"],
    rating: 8.4,
    votes: 1100000,
    runtime: "98 min",
    mood: "Feel-Good",
    overview: "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
    poster: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
    backdrop: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
    trailer_url: "https://www.youtube.com/embed/alIq_wG9fnk"
  }
];

// App State
class CineMindApp {
  constructor() {
    this.movies = FALLBACK_MOVIES;
    this.watchlist = JSON.parse(localStorage.getItem('cinemind_watchlist') || '[]');
    this.currentBaseMovie = FALLBACK_MOVIES[0];
    this.apiAvailable = false;
    
    this.initElements();
    this.initEventListeners();
    this.checkApiAndLoadData();
  }

  initElements() {
    this.movieSelect = document.getElementById('movieSelect');
    this.topNSlider = document.getElementById('topNSlider');
    this.topNVal = document.getElementById('topNVal');
    this.generateRecsBtn = document.getElementById('generateRecsBtn');
    this.moviesGrid = document.getElementById('moviesGrid');
    this.gridSectionTitle = document.getElementById('gridSectionTitle');
    this.targetMovieName = document.getElementById('targetMovieName');
    this.resultCountBadge = document.getElementById('resultCountBadge');
    
    // Search
    this.globalSearchInput = document.getElementById('globalSearchInput');
    this.clearSearchBtn = document.getElementById('clearSearchBtn');
    this.searchSuggestions = document.getElementById('searchSuggestions');
    
    // Hero Elements
    this.heroSpotlight = document.getElementById('heroSpotlight');
    this.heroBackdrop = document.getElementById('heroBackdrop');
    this.heroTitle = document.getElementById('heroTitle');
    this.heroYear = document.getElementById('heroYear');
    this.heroRating = document.getElementById('heroRating');
    this.heroRuntime = document.getElementById('heroRuntime');
    this.heroMood = document.getElementById('heroMood');
    this.heroOverview = document.getElementById('heroOverview');
    this.heroRecommendBtn = document.getElementById('heroRecommendBtn');
    this.heroTrailerBtn = document.getElementById('heroTrailerBtn');
    
    // Modals
    this.movieModal = document.getElementById('movieModal');
    this.modalContent = document.getElementById('modalContent');
    this.closeModalBtn = document.getElementById('closeModalBtn');
    
    this.statsModal = document.getElementById('statsModal');
    this.navStatsBtn = document.getElementById('navStatsBtn');
    this.closeStatsModalBtn = document.getElementById('closeStatsModalBtn');
    
    // Watchlist
    this.navWatchlistBtn = document.getElementById('navWatchlistBtn');
    this.watchlistBadge = document.getElementById('watchlistBadge');
    
    // Mood pills
    this.moodPills = document.querySelectorAll('.mood-pill');
  }

  initEventListeners() {
    // Select & Slider
    this.topNSlider.addEventListener('input', (e) => {
      this.topNVal.textContent = e.target.value;
    });

    this.generateRecsBtn.addEventListener('click', () => {
      const selectedId = parseInt(this.movieSelect.value);
      this.generateRecommendationsFor(selectedId);
    });

    // Hero buttons
    this.heroRecommendBtn.addEventListener('click', () => {
      this.movieSelect.value = this.currentBaseMovie.id;
      this.generateRecommendationsFor(this.currentBaseMovie.id);
      document.querySelector('.recommender-studio').scrollIntoView({ behavior: 'smooth' });
    });

    this.heroTrailerBtn.addEventListener('click', () => {
      this.openMovieModal(this.currentBaseMovie);
    });

    // Global Search
    this.globalSearchInput.addEventListener('input', (e) => {
      const val = e.target.value.trim();
      if (val.length > 0) {
        this.clearSearchBtn.classList.remove('hidden');
        this.showSearchSuggestions(val);
      } else {
        this.clearSearchBtn.classList.add('hidden');
        this.searchSuggestions.classList.add('hidden');
      }
    });

    this.clearSearchBtn.addEventListener('click', () => {
      this.globalSearchInput.value = '';
      this.clearSearchBtn.classList.add('hidden');
      this.searchSuggestions.classList.add('hidden');
    });

    // Mood pills
    this.moodPills.forEach(pill => {
      pill.addEventListener('click', () => {
        this.moodPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const mood = pill.dataset.mood;
        this.filterMoviesByMood(mood);
      });
    });

    // Modal Close
    this.closeModalBtn.addEventListener('click', () => {
      this.movieModal.classList.add('hidden');
      this.modalContent.innerHTML = '';
    });

    this.navStatsBtn.addEventListener('click', () => {
      this.statsModal.classList.remove('hidden');
    });

    this.closeStatsModalBtn.addEventListener('click', () => {
      this.statsModal.classList.add('hidden');
    });

    this.navWatchlistBtn.addEventListener('click', () => {
      this.renderWatchlistGrid();
    });

    // Close modal on click backdrop
    window.addEventListener('click', (e) => {
      if (e.target === this.movieModal) {
        this.movieModal.classList.add('hidden');
        this.modalContent.innerHTML = '';
      }
      if (e.target === this.statsModal) {
        this.statsModal.classList.add('hidden');
      }
    });
  }

  async checkApiAndLoadData() {
    try {
      const res = await fetch('/api/movies');
      if (res.ok) {
        const data = await res.json();
        if (data.status === 'success') {
          this.movies = data.movies;
          this.apiAvailable = true;
          console.log("Connected to Python backend REST API.");
        }
      }
    } catch (e) {
      console.log("Using browser offline similarity engine fallback.");
    }
    
    this.populateMovieSelect();
    this.updateHero(this.movies[0]);
    this.generateRecommendationsFor(this.movies[0].id);
    this.updateWatchlistBadge();
  }

  populateMovieSelect() {
    this.movieSelect.innerHTML = '';
    this.movies.forEach(m => {
      const opt = document.createElement('option');
      opt.value = m.id;
      opt.textContent = `${m.title} (${m.year})`;
      this.movieSelect.appendChild(opt);
    });
  }

  updateHero(movie) {
    this.currentBaseMovie = movie;
    this.heroBackdrop.style.backgroundImage = `url('${movie.backdrop}')`;
    this.heroTitle.textContent = movie.title;
    this.heroYear.innerHTML = `<i class="fa-regular fa-calendar"></i> ${movie.year}`;
    this.heroRating.innerHTML = `<i class="fa-solid fa-star"></i> ${movie.rating} IMDb`;
    this.heroRuntime.innerHTML = `<i class="fa-regular fa-clock"></i> ${movie.runtime}`;
    this.heroMood.textContent = movie.mood;
    this.heroOverview.textContent = movie.overview;
  }

  async generateRecommendationsFor(movieId) {
    const targetMovie = this.movies.find(m => m.id === movieId) || this.movies[0];
    this.updateHero(targetMovie);
    const topN = parseInt(this.topNSlider.value);

    this.gridSectionTitle.innerHTML = `<i class="fa-solid fa-sparkles"></i> Top ML Matches for <span class="accent-text">${targetMovie.title}</span>`;
    this.targetMovieName.textContent = targetMovie.title;

    let recommendations = [];

    if (this.apiAvailable) {
      try {
        const res = await fetch(`/api/recommend?title=${encodeURIComponent(targetMovie.title)}&top_n=${topN}`);
        const data = await res.json();
        if (data.status === 'success') {
          recommendations = data.recommendations;
        }
      } catch (err) {
        console.error(err);
      }
    }

    if (!recommendations.length) {
      recommendations = this.clientSideSimilarityEngine(targetMovie, topN);
    }

    this.renderMoviesGrid(recommendations, true);
  }

  // Client-side fallback similarity matching
  clientSideSimilarityEngine(targetMovie, topN) {
    const targetGenres = new Set(targetMovie.genres);
    const targetDirector = targetMovie.director;
    const targetMood = targetMovie.mood;

    const scored = this.movies
      .filter(m => m.id !== targetMovie.id)
      .map(movie => {
        let score = 0;
        // Shared genres weight
        const sharedGenres = movie.genres.filter(g => targetGenres.has(g));
        score += sharedGenres.length * 0.35;

        // Director weight
        if (movie.director === targetDirector) score += 0.30;
        
        // Mood weight
        if (movie.mood === targetMood) score += 0.25;

        // Base rating influence
        score += (movie.rating / 10) * 0.10;

        const matchPercentage = Math.min(99, Math.max(65, Math.round(score * 100)));

        const reasons = [];
        if (sharedGenres.length) reasons.append(`Shared genres (${sharedGenres.join(', ')})`);
        if (movie.director === targetDirector) reasons.append(`Directed by ${movie.director}`);
        if (movie.mood === targetMood) reasons.append(`Matching mood: ${movie.mood}`);

        return {
          ...movie,
          similarity_score: score,
          match_percentage: matchPercentage,
          match_reasons: reasons.length ? reasons : ["High thematic plot correlation"]
        };
      });

    scored.sort((a, b) => b.match_percentage - a.match_percentage);
    return scored.slice(0, topN);
  }

  renderMoviesGrid(movieList, isRecommendation = false) {
    this.moviesGrid.innerHTML = '';
    this.resultCountBadge.textContent = `${movieList.length} movies`;

    if (!movieList.length) {
      this.moviesGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: var(--text-muted);">
          <i class="fa-solid fa-film" style="font-size: 3rem; margin-bottom: 1rem;"></i>
          <p>No matching movies found.</p>
        </div>`;
      return;
    }

    movieList.forEach(movie => {
      const card = document.createElement('div');
      card.className = 'movie-card';
      const isSaved = this.watchlist.some(w => w.id === movie.id);

      card.innerHTML = `
        <div class="poster-wrapper">
          <img src="${movie.poster}" alt="${movie.title}" loading="lazy" />
          ${movie.match_percentage ? `<div class="match-badge"><i class="fa-solid fa-bolt"></i> ${movie.match_percentage}% Match</div>` : ''}
          <div class="card-overlay">
            <button class="quick-view-btn"><i class="fa-solid fa-circle-info"></i> View Details</button>
          </div>
        </div>
        <div class="card-content">
          <h3 class="movie-card-title" title="${movie.title}">${movie.title}</h3>
          <div class="card-meta-row">
            <span><i class="fa-regular fa-calendar"></i> ${movie.year}</span>
            <span class="rating-star"><i class="fa-solid fa-star"></i> ${movie.rating}</span>
          </div>
          <div class="card-genres">
            ${movie.genres.slice(0, 2).map(g => `<span class="genre-tag">${g}</span>`).join('')}
          </div>
        </div>
      `;

      card.addEventListener('click', () => {
        this.openMovieModal(movie);
      });

      this.moviesGrid.appendChild(card);
    });
  }

  filterMoviesByMood(mood) {
    if (mood === 'all') {
      this.gridSectionTitle.innerHTML = `<i class="fa-solid fa-globe"></i> Full Movie Catalog`;
      this.renderMoviesGrid(this.movies);
      return;
    }

    const filtered = this.movies.filter(m => m.mood.toLowerCase() === mood.toLowerCase());
    this.gridSectionTitle.innerHTML = `<i class="fa-solid fa-compass"></i> Mood: <span class="accent-text">${mood}</span>`;
    this.renderMoviesGrid(filtered);
  }

  showSearchSuggestions(query) {
    const q = query.toLowerCase();
    const matches = this.movies.filter(m => 
      m.title.toLowerCase().includes(q) || 
      m.director.toLowerCase().includes(q) ||
      m.genres.some(g => g.toLowerCase().includes(q))
    );

    this.searchSuggestions.innerHTML = '';
    if (!matches.length) {
      this.searchSuggestions.classList.add('hidden');
      return;
    }

    matches.slice(0, 5).forEach(movie => {
      const item = document.createElement('div');
      item.className = 'suggestion-item';
      item.innerHTML = `
        <img src="${movie.poster}" alt="${movie.title}" />
        <div class="suggestion-info">
          <div class="suggestion-title">${movie.title} (${movie.year})</div>
          <div class="suggestion-sub">${movie.genres.join(', ')} • Dir. ${movie.director}</div>
        </div>
      `;

      item.addEventListener('click', () => {
        this.searchSuggestions.classList.add('hidden');
        this.globalSearchInput.value = movie.title;
        this.openMovieModal(movie);
      });

      this.searchSuggestions.appendChild(item);
    });

    this.searchSuggestions.classList.remove('hidden');
  }

  openMovieModal(movie) {
    const isSaved = this.watchlist.some(w => w.id === movie.id);

    this.modalContent.innerHTML = `
      <div class="modal-hero">
        <iframe src="${movie.trailer_url}?autoplay=1&mute=0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      </div>
      <div class="modal-detail-container">
        <div class="modal-title-row">
          <div>
            <h2 class="modal-title">${movie.title}</h2>
            <div class="modal-meta-bar">
              <span><i class="fa-regular fa-calendar"></i> ${movie.year}</span>
              <span class="rating-star"><i class="fa-solid fa-star"></i> ${movie.rating} IMDb (${movie.votes.toLocaleString()} votes)</span>
              <span><i class="fa-regular fa-clock"></i> ${movie.runtime}</span>
              <span class="mood-tag">${movie.mood}</span>
            </div>
          </div>
          <button id="toggleWatchlistModalBtn" class="btn ${isSaved ? 'btn-secondary' : 'btn-primary'}">
            <i class="fa-solid ${isSaved ? 'fa-check' : 'fa-bookmark'}"></i> ${isSaved ? 'In Watchlist' : 'Add to Watchlist'}
          </button>
        </div>

        <p class="modal-overview">${movie.overview}</p>

        <div class="modal-crew-grid">
          <div><span class="crew-label">Director</span></div>
          <div>${movie.director}</div>
          <div><span class="crew-label">Cast</span></div>
          <div>${movie.cast.join(', ')}</div>
          <div><span class="crew-label">Genres</span></div>
          <div>${movie.genres.join(', ')}</div>
        </div>

        <div style="margin-top: 20px;">
          <button id="recommendFromModalBtn" class="btn btn-gradient">
            <i class="fa-solid fa-wand-magic-sparkles"></i> Get Movies Similar to ${movie.title}
          </button>
        </div>
      </div>
    `;

    document.getElementById('toggleWatchlistModalBtn').addEventListener('click', () => {
      this.toggleWatchlist(movie);
      this.openMovieModal(movie); // refresh modal state
    });

    document.getElementById('recommendFromModalBtn').addEventListener('click', () => {
      this.movieModal.classList.add('hidden');
      this.movieSelect.value = movie.id;
      this.generateRecommendationsFor(movie.id);
      document.querySelector('.recommender-studio').scrollIntoView({ behavior: 'smooth' });
    });

    this.movieModal.classList.remove('hidden');
  }

  toggleWatchlist(movie) {
    const idx = this.watchlist.findIndex(w => w.id === movie.id);
    if (idx > -1) {
      this.watchlist.splice(idx, 1);
    } else {
      this.watchlist.push(movie);
    }
    localStorage.setItem('cinemind_watchlist', JSON.stringify(this.watchlist));
    this.updateWatchlistBadge();
  }

  updateWatchlistBadge() {
    this.watchlistBadge.textContent = this.watchlist.length;
  }

  renderWatchlistGrid() {
    this.gridSectionTitle.innerHTML = `<i class="fa-solid fa-bookmark"></i> My Watchlist`;
    this.renderMoviesGrid(this.watchlist);
  }
}

// Instantiate on DOM load
document.addEventListener('DOMContentLoaded', () => {
  window.app = new CineMindApp();
});
