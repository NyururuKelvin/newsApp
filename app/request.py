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

def get_source():
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

def process_sources(sources_list):
    '''
    Function  that processes the sources result and transforms them to a list of Objects
    '''
    sources_results = []
    for sources in source_list:
        id=sources.get('id')
        name=sources.get('name')
        description=sources.get('description')
        url=sources.get('url')
        
        if description:
            new_source=Source(id,name,description,url)
            source_results.append(new_source)

    return source_results

def get_articles(source_id):
    get_articles_url = base_url_article.format(source_id, api_key)
    res = requests.get(get_articles_url)
    articles_data = res.json().get('articles')

    return process_articles(articles_data)

def process_articles(articles_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    articles = []
    if articles_list:
        for article in articles_list:
            # article = Article(article['id'], article['name'], article['author'], article['title'], article['description'], article['url'], article['urlToImage'], article['publishedAt'], article['content'])
            articles.append(article)
        return articles