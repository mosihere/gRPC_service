import requests
import json


def get_movie_info():
    """
        function to send a "GET" HTTP request
        and get top 250 movies of IMDB
        then serializing it and dump it in a json file    
    """

    API_KEY = 'YOUR-API-KEY'
    url = f'https://imdb-api.com/en/API/Top250Movies/{API_KEY}'

    # Delete unnecessary info from data
    response = requests.get(url)
    data = response.json()['items']
    for item in data:
        del item['id']
        del item['fullTitle']
        del item['year']
        del item['image']
        del item['crew']

    dict_data = {}
    dict_data['items'] = data
    
    with open('Top250Movies.json', 'w') as f:
        json.dump(dict_data, f)

    return response.status_code




if __name__ == "__main__":
    print('Top 250 Movies:\n')
    print(get_movie_info())
