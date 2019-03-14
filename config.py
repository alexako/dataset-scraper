import os

# https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/
API_KEY = os.environ.get('BING_SEARCH_API_KEY')

ENDPOINT = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
MAX_RESULTS = 250
GROUP_SIZE = 50
