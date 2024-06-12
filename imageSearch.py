# https://developers.google.com/custom-search/v1/overview for CSE
# CSE ID https://cse.google.com/cse/create/new

import requests

class ImageSearch:

    def __init__(self):
        # self.cse_id = cse_id
        # self.api_key = api_key
        # self.search_type = search_type
        # self.search_item = search_item3
        pass

    def searchFunction(self, cse_id, api_key, search_type, search_item):

        url = f"https://www.googleapis.com/customsearch/v1?q={search_item} {search_type} cover&num=1&start=1&imgSize=huge&searchType=image&key={api_key}&cx={cse_id}"

        response = requests.get(url)
        response.raise_for_status()

        search_results = response.json()
        image_url = search_results['items'][0]['link']

        print('Image URL:', image_url)