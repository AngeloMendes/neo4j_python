from __future__ import annotations


from neomodel import StructuredNode, StringProperty, RelationshipTo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from author import AuthorModel


class BookModel(StructuredNode):
    title = StringProperty(unique_index=True)
    author = RelationshipTo('neomodel_models.author.AuthorModel', 'WRITE')

    @classmethod
    def _search(cls, title):
        return cls.nodes.filter(title=title)

    @classmethod
    def _create(cls, title):
        return cls(title=title).save()

    def author_connect(self, author: AuthorModel):
        return self.author.connect(author)
