import urllib.request,json
from app.models import Source,Article
import requests

# Getting api key
api_key = None

# Getting base urls
highlights_url=None
sources_url=None
search_url=None


def configure_request(app):
    global api_key,highlights_url,sources_url,search_url

    api_key = app.config['NEWS_API_KEY']
    highlights_url=app.config['HEADLINES_API_URL']
    sources_url=app.config['SOURCE_API_URL']
    search_url=app.config['SEARCH_SOURCES']

def get_sources():
    '''
    Function that gets the json response from our url request
    '''
    source_api_url=sources_url.format(api_key)

    with urllib.request.urlopen(source_api_url) as url:
        unread_data=url.read()
        read_json=json.loads(unread_data)

        source_results=None

        if read_json['sources']:
            sources_list=read_json['sources']
            source_results=process_results(sources_list)

    return source_results

def process_results(sources_list):
    '''
    Function  that processes the sources result and transforms them to a list of Objects
    '''
    source_results = []
    for sources in sources_list:
        id=sources.get('id')
        name=sources.get('name')
        description=sources.get('description')
        url=sources.get('url')
        
        if description:
            new_source=Source(id,name,description,url)
            source_results.append(new_source)

    return source_results

def get_article(source_id):
    get_highlights_url=highlights_url.format(api_key)

    with urllib.request.urlopen(get_highlights_url) as url:
        get_data=url.read()
        get_json_data=json.loads(get_data)

        articles_data=None

        if get_json_data['articles']:
            articles_list=get_json_data['articles']
            articles_data=process_article(articles_list)
        
    return articles_data

def process_article(articles_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    articles_data=[]

    for article in articles_list:
        id=article.get('id')
        name=article.get('name')
        urlToImage=article.get('urlToImage')
        description=article.get('description')
        publishedAt=article.get('publishedAt')
        url=article.get('url')
        title=article.get('title')
        source=article.get('source')
        if description:
            new_article=Article(id,name,urlToImage,description,title,url,publishedAt,source)
            articles_data.append(new_article)

    return articles_data

def search_for_article(article):
    search_article_url=search_url.format(article,api_key)

    with urllib.request.urlopen(search_article_url) as url:
        search_data=url.read()
        search_json=json.loads(search_data)

        search_article=None

        if search_json['articles']:
            searches=search_json['articles']
            search_article=process_article(searches)

    return search_article