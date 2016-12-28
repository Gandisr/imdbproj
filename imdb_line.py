import json
import requests, http.client


class Imdb_Line:

    def __init__(self, api_id):
        self.api_id = api_id;


    #
    # def get_api_id(self):
    #     conn = http.client.HTTPSConnection("api.themoviedb.org")
    #     payload = "{}"
    #
    #     api_str = "/3/find/tt"
    #     api_str += str(self.imdb_id)
    #     api_str += "?api_key="
    #     api_str += "90f196cfd75d24a642ead21588895dd4"
    #     api_str += "&language=en-US&external_source=imdb_id"
    #     conn.request("GET", api_str)
    #     res = conn.getresponse()
    #     data = res.read()
    #

    def get_json_overview(self):
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        payload = "{}"
        api_str = "/3/movie/"
        api_str += str(self.api_id)
        api_str += "?api_key="
        api_str += "90f196cfd75d24a642ead21588895dd4"
        conn.request("GET", api_str)
        res = conn.getresponse()
        if '404' in res.getheader('status'):
            return None
        data = res.read()

        return data


    def get_json_cast(self):
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        payload = "{}"
        api_str = "/3/movie/"
        api_str += str(self.api_id)
        api_str += "/credits/"
        api_str += "?api_key="
        api_str += "90f196cfd75d24a642ead21588895dd4"
        conn.request("GET", api_str)
        res = conn.getresponse()
        if '404' in res.getheader('status'):
            return None
        data = res.read()

        return data


    def json_decoder(self):
        j = self.get_json_overview()
        if(j != None):
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

