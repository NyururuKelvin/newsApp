import urllib.request,json
from app.models import Source,Article

# Getting api key
api_key = None
# Getting the news base url
base_url = None
# Getting the articles base url
base_url_article = None

def configure_request(app):
    global api_key,base_url,base_url_article
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['NEWS_SOURCE_BASE_URL']
    base_url_article = app.config['ARTICLES_BASE_URL']