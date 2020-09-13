from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_sources, get_articles


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    sources = get_sources()
    return render_template('index.html', sources = sources)
    

@main.route('/articles/<source_id>')
def articles(source_id):
    articles = get_articles(source_id)
    return render_template('article.html', articles=articles)