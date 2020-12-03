import requests
from iskabot.api.status_codes import *

import random

class TenorException(Exception):
    pass

class TenorGIFNotFoundException(Exception):
    pass

class TenorFetcher():
    def __init__(self, api_key):
        self.api_key = api_key

    def search_gif(self, search_term, out_of = 8):
        request_endpoint = f"https://api.tenor.com/v1/search"
        response = requests.get(request_endpoint, params={
            "q" : search_term,
            "limit" : 8,
            "api_key" : self.api_key
        })

        if response.status_code == HTTP_NOT_FOUND_404:
            raise TenorGIFNotFoundException("Error 404: GIF by this search term not found")
        elif response.status_code != HTTP_SUCCESS_200:
            raise TenorException("Error fetching GIF")

        data = random.choice(response.json().get("results"))
        tinygif = data.get("media")[0].get("gif").get("url")
        return tinygif