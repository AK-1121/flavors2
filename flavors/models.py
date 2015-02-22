from django.db import models
from django.template.defaultfilters import slugify

RAITINGS = (('0', 'x'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),  ('5', '5'))
#RAITINGS = ('x', '1', '2', '3', '4', '5')

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Flavor(TimeStampedModel):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=200, default='xxx')
    tested = models.BooleanField(default=False)
    short_title = models.SlugField(max_length=50, default='')
    raiting = models.CharField(max_length=10, choices=RAITINGS,
                               default=RAITINGS[0])

    # Override standart save() method 
    # (Check before saving, that field "tested" is True, if field raiting 
    # was determined: 
    def save(self, *args, **kwargs):
        self.short_title = slugify(self.title)
        if self.raiting != 'x':
            self.tested = True
        # Call the real save() method:
        super(Flavor, self).save(*args, **kwargs)
