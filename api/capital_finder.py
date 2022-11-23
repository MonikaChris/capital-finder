from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        print(query_string_list)
        dic = dict(query_string_list)

        country = dic["country"]

        url = "https://restcountries.com/v2/name/"
        r = requests.get(url + dic["country"])
        data = r.json()
        print(data)
        capital = data[0]['capital']
        message = f'The capital of {dic["country"]} is {capital}.'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
