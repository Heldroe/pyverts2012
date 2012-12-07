from haystack import indexes
from elements.models import Element

class ElementIndex (indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True)
    element = indexes.EdgeNgramField(use_template=True)

    def get_model (self):
        return Element

    def index_queryset (self):
        return self.get_model().objects.all()