import urllib.request,json
from app.models import Source,Article
import requests

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

def get_sources():
    '''
    Function that gets the json response from our url request
    '''
    get_source_url = base_url.format(api_key)
    res = requests.get(get_source_url)
    data = res.json().get('sources')
    return process_sources(data)

def process_sources(sources_list):
    '''
    Function  that processes the sources result and transforms them to a list of Objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        county = source_item.get('country')
        
        if url:
            sources_object = Source(id, name, description, url, category, language, county)
            sources_results.append(sources_object)
        
    return sources_results