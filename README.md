# gRPC Service

using gRPC in Python 

## Application
__Whenever client send a request, server will process it and send JSON object as response back to the client__
**Response is --> Top 250 Movies of IMDB**

## Clone Project


```bash
$ sudo apt install git
$ git clone https://github.com/mosihere/gRPC_service
```

## Usage
after cloning project:
you should register in [imdb](https://imdb-api.com/) and take an API-KEY
or use Top250Movies.json
create an virtual environment,
activate it, install dependencies and done.

```
$ cd gRPC_service
$ python3 -m virtualenv .venv
$ source bin/activate/.venv
$ python -m pip install -r requirements.txt
```

## Running Program
```
first run the Server:
$ python movie_server.py

in another terminal run the client:
$ python movie_client.py
```
## Contributing
Pull requests are welcome.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
