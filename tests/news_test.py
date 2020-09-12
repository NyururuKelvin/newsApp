import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    def setUp(self):

        '''
        Set up method that will run before every Test

        '''

        self.new_source = Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")
    
    def test_isSourceInstance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):

        self.assertEquals(self.new_source.id,'abc-news')
        self.assertEquals(self.new_source.name,'ABC News')
        self.assertEquals(self.new_source.description,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEquals(self.new_source.url,'https://abcnews.go.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.language,'en')
        self.assertEquals(self.new_source.country,'us')

#test class for the articles
class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("bbc-news", "BBC News", "BBC News", "States partly reopen as US virus deaths top 50,000", "Georgia, Oklahoma and Alaska lift some restrictions despite warnings that it may be too soon.","http://www.bbc.co.uk/news/world-us-canada-52421730", 'null', "2020-04-25T04:39:19Z","Image businesses to reopen after measures imposed to fight the coronavirus")

    def test_isArticleInstance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_to_check_instance_variables(self):
        
        self.assertEquals(self.new_article.id,'bbc-news')
        self.assertEquals(self.new_article.name,'BBC News')
        self.assertEquals(self.new_article.author,'BBC News')
        self.assertEquals(self.new_article.title,'States partly reopen as US virus deaths top 50,000')
        self.assertEquals(self.new_article.description,'Georgia, Oklahoma and Alaska lift some restrictions despite warnings that it may be too soon.')
        self.assertEquals(self.new_article.url,'http://www.bbc.co.uk/news/world-us-canada-52421730')
        self.assertEquals(self.new_article.urlToImage, 'null')
        self.assertEquals(self.new_article.publishedAt,'2020-04-25T04:39:19Z')
        self.assertEquals(self.new_article.content,'Image businesses to reopen after measures imposed to fight the coronavirus' )

if __name__ == '__main__':
    unittest.main()