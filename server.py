import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from model import MovieRecommender

# Force stdout encoding for Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Global Recommender instance
recommender = MovieRecommender()

class MovieAppRequestHandler(SimpleHTTPRequestHandler):
    """Custom HTTP Request Handler serving static web files and REST API."""

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        # REST API Endpoints
        if path.startswith("/api/"):
            self.handle_api(path, query)
            return

        # Serve static web files from current directory
        if path == "/" or path == "":
            self.path = "/index.html"
            
        return super().do_GET()

    def handle_api(self, path: str, query: dict):
        """Process API endpoints and return JSON response."""
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

        response_data = {}

        if path == "/api/movies":
            response_data = {
                "status": "success",
                "total": len(recommender.get_movies()),
                "movies": recommender.get_movies(),
                "genres": recommender.get_genres(),
                "moods": recommender.get_moods()
            }
        elif path == "/api/recommend":
            title = query.get("title", ["Inception"])[0]
            top_n = int(query.get("top_n", [6])[0])
            response_data = recommender.get_recommendations(title, top_n=top_n)

        elif path == "/api/search":
            q = query.get("q", [""])[0]
            movies = recommender.search_movies(q)
            response_data = {
                "status": "success",
                "query": q,
                "count": len(movies),
                "movies": movies
            }

        elif path == "/api/mood":
            mood = query.get("mood", ["all"])[0]
            movies = recommender.filter_by_mood(mood)
            response_data = {
                "status": "success",
                "mood": mood,
                "count": len(movies),
                "movies": movies
            }

        elif path == "/api/stats":
            response_data = {
                "status": "success",
                "stats": recommender.get_model_stats()
            }
        else:
            response_data = {
                "status": "error",
                "message": f"Endpoint '{path}' not found."
            }

        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode("utf-8"))

    def do_OPTIONS(self):
        """Handle CORS pre-flight requests."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def run_server(port: int = 8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MovieAppRequestHandler)
    print(f"==================================================")
    print(f"🎬 Movie Recommender Server running on http://localhost:{port}")
    print(f"Press Ctrl+C to stop.")
    print(f"==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    run_server(port)
