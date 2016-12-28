import json
import requests


class Imdb_Line:

    def __init__(self, imdb_id):
        self.imdb_id = imdb_id

    def create_api_request_overview(self):
        api_request = "https://api.themoviedb.org/3/find/tt"
        api_request += str(self.imdb_id)
        api_request += "?api_key="
        api_request += "api_key_placeholder"
        api_request += "&language=en-US&external_source=imdb_id"
        return api_request

    def get_json_overview(self):
        request_str = self.create_api_request_overview()
        response = requests.get(request_str)
        return response.json()

    def create_api_request_cast(self):
        api_request = "https://api.themoviedb.org/3/find/tt"
        api_request += str(self.imdb_id)
        api_request += "credits?api_key="
        api_request += "api_key_placeholder"
        api_request += "&language=en-US&external_source=imdb_id"
        return api_request

    def get_json_cast(self):
        request_str = self.create_api_request_cast()
        response = requests.get(request_str)
        return response.json()

    def json_decoder(self):
        j = self.get_json_overview()
        imdb_json = json.load(j)
        self.budget = imdb_json['budget']
        self.gross = imdb_json['revenue']
        self.title = imdb_json['original_title']
        self.imdb_rating = imdb_json['vote_average']
        self.year = imdb_json['release_date'][:4]

        j = self.get_json_cast()
        imdb_json = json.load(j)

        self.cast = []
        cast_arr = imdb_json['cast']
        for sub_j in cast_arr:
            self.cast.append(sub_j['name'])

