import grpc
import json
from concurrent import futures
from movie_service_pb2 import MovieResponse

import movie_service_pb2_grpc as pb2_grpc

# Load our JSON file --> JSON objects converts to Dictionary
with open('Top250Movies.json') as f:
    data = json.load(f)

# print(type(data))
# print(data['items'])


class MoviesService(pb2_grpc.MoviesServicer):

    def get_movies(self, request, context):
        select_all_movies = request.movie_list
        return MovieResponse(movies=data.get(select_all_movies))

# sample_data = {"items":[{"rank":"1", "title":"Shawshank Redemption", "imDbRating":"9.8", "imDbRatingCount":"20183"}, {"rank":"2", "title":"12 Angry Men", "imDbRating":"9.6", "imDbRatingCount":"212214"} ]}


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MoviesServicer_to_server(MoviesService(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print('gRPC server is running...')
    serve()