from src.py2neo_models.product import ProductModel
from src.py2neo_models.order import OrderModel
import sys

from unittest import TestCase

sys.path.append('/home/accurate/Project/test_neo4j/src/')


class TestProduct(TestCase):

    def test_unit(self):
        product = ProductModel(name="new product", cost=1.0)
        self.assertEqual('new product', product.name)
        self.assertEqual(1, product.cost)

    def test_create(self):
        product = ProductModel(name="new product 2", cost=1.0)
        ProductModel._create(product)
        product = ProductModel._search(name="new product 2")
        self.assertEqual('new product 2', product.name)
        self.assertEqual(1, product.cost)

    def test_create_relationship(self):
        product = ProductModel(name="new product 3", cost=1.0)
        ProductModel._create(product)
        OrderModel._create(title="new order")
        order = OrderModel._search(title="new order")
        product = ProductModel._search(name="new product 3")
        product.sold.add(order)
        ProductModel._update(product)
        product = ProductModel._search(name="new product 3")
        self.assertEqual('new product 3', product.name)
        self.assertEqual(1, product.cost)
        self.assertIsNotNone(product.sold)
        self.assertEqual("new order", list(product.sold)[0].title)


