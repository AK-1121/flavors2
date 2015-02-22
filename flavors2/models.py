from django.db import models
from django.utils import timezone

from flavors.models import Flavor

class PublishedManager(models.Manager):

    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(pub_date__lte=timezone.now(), **kwargs)
        #return self.filter(pub_date__gt=timezone.now(), **kwargs)

    def not_published(self, **kwargs):
        return self.filter(pub_date_gt=timezone.now(), **kwargs)

class FlavorReview(models.Model):
    title = models.ForeignKey(Flavor)
    review = models.CharField(max_length=255, default='')
    pub_date = models.DateTimeField(auto_now_add=True)


    objects = PublishedManager()

