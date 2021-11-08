
from neomodel import StructuredNode, StringProperty, RelationshipFrom


class AuthorModel(StructuredNode):
    name = StringProperty(unique_index=True)
    books = RelationshipFrom('neomodel_models.book.BookModel', 'WRITTEN BY')

    @classmethod
    def _search(cls, name):
        return cls.nodes.filter(name=name)

    @classmethod
    def _create(cls, name):
        return cls(name=name).save()
