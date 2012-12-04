from haystack import indexes
from profiles.models import UserProfile

class UserProfileIndex (indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)

    def get_model (self):
        return UserProfile

    def index_queryset (self):
        return self.get_model().objects.all()