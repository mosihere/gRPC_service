import json
import unittest
from imdb_api import get_movie_info
from movie_server import MoviesService
from movie_service_pb2 import MovieList, MovieRequest, MovieResponse


class TestApis(unittest.TestCase):
    def test_imdb_get_request(self):
        """
        Test that sending a GET request for imdb is working.
        """
        status_code = get_movie_info()
        self.assertEqual(status_code, 200)


    # def test_movie_server(self):
    #     service = MoviesService()
    #     with open('Top250Movies.json') as f:
    #         data = json.load(f)
    #     request = MovieRequest(movie_list=str(data))
    #     response = service.get_movies(request, None)


if __name__ == "__main__":
    unittest.main()
