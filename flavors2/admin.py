from django.contrib import admin

from flavors2.models import FlavorReview
from flavors.admin import FlavorAdmin


class FlavorReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'pub_date')

admin.site.register(FlavorReview, FlavorReviewAdmin)
