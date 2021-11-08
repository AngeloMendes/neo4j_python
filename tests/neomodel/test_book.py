import neomodel
from src.neomodel_models.book import BookModel
import sys

from os import getenv
from dotenv import load_dotenv
from neomodel import config

from unittest import TestCase

sys.path.append('/home/accurate/Project/test_neo4j/src/')


class TestBook(TestCase):

    def resource(self):
        load_dotenv()
        config.DATABASE_URL = getenv('TEST_URL_DB')

    def test_unit(self):
        book = BookModel(title='new book')
        assert 'new book' == book.title

    def test_create(self):
        self.resource()
        book = BookModel._create(title='book')
        self.assertEqual('book', book.title)
        self.assertIsNotNone(book.id)

    def test_search(self):
        self.resource()
        book = BookModel._create(title='book_search')
        book = BookModel.nodes.first(title="book_search")
        self.assertIsNotNone(book)
        self.assertEqual('book_search', book.title)
        self.assertIsNotNone(book.id)

        book = BookModel._search(title='book_search')
        self.assertIsNotNone(book)

