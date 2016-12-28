import json
import http.client

class Imdb_Line:

    def __init__(self, api_id):
        self.api_id = api_id;
        self.budget = 0;
        self.gross = 0;
        self.title = ''
        self.year = ''
        self.imdb_rating = 0.0
        self.cast = []
        self.null_row = False


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
        if '200' not in res.getheader('status'):
            return None
        data = res.read()

        return data.decode("utf-8")


    def get_json_cast(self):
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        payload = "{}"
        api_str = "/3/movie/"
        api_str += str(self.api_id)
        api_str += "/credits"
        api_str += "?api_key="
        api_str += "90f196cfd75d24a642ead21588895dd4"
        conn.request("GET", api_str ,payload)
        res = conn.getresponse()
        if '200' not in res.getheader('status'):
            return None
        data = res.read()

        return data.decode("utf-8")


    def json_decoder(self):
        j = self.get_json_overview()
        if j is not None:
            imdb_json = json.loads(j)
            self.budget = imdb_json['budget']
            self.gross = imdb_json['revenue']
            self.title = imdb_json['original_title']
            self.imdb_rating = imdb_json['vote_average']
            self.year = imdb_json['release_date'][:4]
        else:
            self.null_row = True
        j = self.get_json_cast()
        if j is not None:
            imdb_json = json.loads(j)
            cast_arr = imdb_json['cast']
            for sub_j in cast_arr:
                self.cast.append(sub_j['name'])
        else:
            self.null_row = True

    def csv_line(self):
        res ={}
        res['Title'] = self.title
        res['Year'] = self.year
        res['Budget']= str(self.budget)
        res['Gross']= str(self.gross)
        res['IMDB_rating'] = str(self.imdb_rating)
        res['Cast'] = str(self.cast)
        return res

    def getNewLine(self):
        self.json_decoder()
        if self.null_row:
            return None
        else:
            return self.csv_line()

    def __str__(self):
        res = ""
        res += "Title = " + self.title
        res += " year = " + self.year
        res += " Budget = " + str(self.budget)
        res += " Cast = " + str(self.cast)
        return res






