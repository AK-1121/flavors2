from django.contrib import admin
from flavors.models import Flavor

def raitings_reset(modeladmin, request, queryset):
    queryset.update(raiting='x', tested=False)
raitings_reset.short_description = "Reset raitings."


class FlavorAdmin(admin.ModelAdmin):
    #fieldsets = 
    list_display = ('title', 'short_title', 'color', 'tested', 'raiting', 
                    'created', 'modified')
    list_per_page = 10
    ordering = ['title']
    actions = [raitings_reset]
    # prepopulated_fields позволяет определить поля, которые получают значение
    # основываясь на значениях других полей:
    #prepopulated_fields = {"short_title": ("title",)}

admin.site.register(Flavor, FlavorAdmin)
