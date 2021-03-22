from django.contrib import admin
from .models import *



class AdImageInline(admin.TabularInline):
    model = AdverImage
    fields = ('image', 'description')


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [AdImageInline, ]

admin.site.register(Topper)
admin.site.register(Commentary)