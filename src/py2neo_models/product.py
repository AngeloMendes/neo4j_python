from py2neo.ogm import Model, Property, RelatedTo, GraphObject
from src.base import graph_db
#from base import graph_db


class ProductModel(GraphObject):
    #__primarykey__ = "name"

    name = Property()
    cost = Property()

    sold = RelatedTo('py2neo_models.order.OrderModel', 'Sold')

    def __init__(self, name, cost, sold=None, *values, **properties):
        super().__init__(*values, **properties)
        self.name = name
        self.cost = cost
        self.sold = sold

    @classmethod
    def _create(cls, product):
        graph_db.create(product)

    @classmethod
    def _update(cls, product):
        #graph_db.update(product)
        graph_db.push(product)

    @classmethod
    def _search(cls, name):
        return ProductModel.wrap(graph_db.nodes.match("ProductModel", name=name).first())


