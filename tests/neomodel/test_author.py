from os import getenv
from dotenv import load_dotenv
import neomodel
from src.neomodel_models.author import AuthorModel
from neomodel import config
from unittest import TestCase

import sys

sys.path.append('/home/accurate/Project/test_neo4j/src/')


class TestAuthor(TestCase):

    #@pytest.fixture()
    def resource(self):
        load_dotenv()
        config.DATABASE_URL = getenv('URL_DB')

    def test_unit(self):
        author = AuthorModel(name='author')
        assert 'author' == author.name

    def test_create(self):
        self.resource()
        author = AuthorModel._create(name='author 2')
        self.assertEqual('author 2', author.name)
        self.assertIsNotNone(author.id)

    def test_search(self):
        self.resource()
        author = AuthorModel._create(name='author_search')
        author = AuthorModel.nodes.first(name="author_search")
        self.assertIsNotNone(author)
        self.assertEqual('author_search', author.name)
        self.assertIsNotNone(author.id)

        author = AuthorModel._search(name='author_search')
        self.assertIsNotNone(author)


