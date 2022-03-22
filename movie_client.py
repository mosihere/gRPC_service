import grpc
from movie_service_pb2 import MovieRequest
from movie_service_pb2_grpc import MoviesStub



class FetchMovies:
    def __init__(self) -> None:
        self.channel = grpc.insecure_channel('localhost:50051')
        self.client = MoviesStub(self.channel)

    def get_movies(self, movie_list):
        request = MovieRequest(movie_list=movie_list)
        response = self.client.get_movies(request)
        return response




if __name__ == "__main__":
    client = FetchMovies()
    print(client.get_movies('items'))