from django.contrib import admin
from .models import Presentation, Presenter


class PresenterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Presenter, PresenterAdmin)


class PresentationAdmin(admin.ModelAdmin):
    list_filter = ('presenter', 'length')

admin.site.register(Presentation, PresentationAdmin)
