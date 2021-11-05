from py2neo.ogm import Model, Property, RelatedFrom, GraphObject
from src.base import graph_db
#from base import graph_db


class OrderModel(GraphObject):
    # __primarykey__ = "title"

    title = Property()
    tag_line = Property("tagline")
    released = Property()

    products = RelatedFrom("py2neo_models.product.ProductModel", "Product")

    def __init__(self, title, tag_line=None, released=None, *values, **properties):
        super().__init__(*values, **properties)
        self.title = title
        self.tag_line = tag_line
        self.released = released

    @classmethod
    def _create(cls, title):
        tx = graph_db.begin()
        tx.create(cls(title))
        graph_db.commit(tx)

    @classmethod
    def _search(cls, title):
        return OrderModel.wrap(graph_db.nodes.match("OrderModel", title=title).first())

    @classmethod
    def _update(cls, order):
        graph_db.push(order)
