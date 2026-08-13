import sys
from model import MovieRecommender

# Force standard utf-8 print compatibility on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_tests():
    print("--------------------------------------------------")
    print("Running Automated Verification Tests for model.py")
    print("--------------------------------------------------")
    
    recommender = MovieRecommender()
    stats = recommender.get_model_stats()
    
    assert stats['total_movies'] > 0, "Total movies should be greater than 0"
    assert stats['vocabulary_size'] > 0, "Vocabulary size should be greater than 0"
    print(f"[OK] Model stats verified: {stats['total_movies']} movies, matrix shape {stats['matrix_shape']}")
    
    # Test 1: Inception recommendations
    res = recommender.get_recommendations("Inception", top_n=3)
    assert res['status'] == 'success', "Recommendation status should be success"
    assert len(res['recommendations']) == 3, "Should return 3 recommendations"
    titles = [m['title'] for m in res['recommendations']]
    print(f"[OK] 'Inception' Recommendations: {titles}")
    
    # Test 2: Search functionality
    search_res = recommender.search_movies("Nolan")
    assert len(search_res) >= 3, "Christopher Nolan search should return at least 3 movies"
    print(f"[OK] 'Nolan' Search matched {len(search_res)} movies")
    
    # Test 3: Mood filtering
    mood_res = recommender.filter_by_mood("Mind-Bending")
    assert len(mood_res) > 0, "Mood filter 'Mind-Bending' should return movies"
    print(f"[OK] Mood filter 'Mind-Bending' matched {len(mood_res)} movies")
    
    print("\n[SUCCESS] ALL TESTS PASSED!")

if __name__ == "__main__":
    run_tests()
