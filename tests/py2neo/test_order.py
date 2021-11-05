from src.py2neo_models.order import OrderModel
from src.py2neo_models.product import ProductModel
import sys

from unittest import TestCase

sys.path.append('/home/accurate/Project/test_neo4j/src/')


class TestProduct(TestCase):

    def test_unit(self):
        order = OrderModel(title="new order", cost=1.0)
        self.assertEqual('new order', order.title)
        self.assertEqual(1, order.cost)

    def test_create(self):
        OrderModel._create(title="new order 2")
        order = OrderModel._search(title="new order 2")
        self.assertEqual('new order 2', order.title)

    def test_create_relationship(self):
        product = ProductModel(name="new product", cost=1.0)
        ProductModel._create(product)
        OrderModel._create(title="new order 3")
        order = OrderModel._search(title="new order 3")
        product = ProductModel._search(name="new product")
        order.products.add(product)
        OrderModel._update(order)
        order = OrderModel._search(title="new order 3")

        self.assertIsNotNone(order.products)
        self.assertEqual('new product', list(order.products)[0].name)
        self.assertEqual(1, list(order.products)[0].cost)
