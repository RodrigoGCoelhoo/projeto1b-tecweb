from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tagslist', views.tagsList, name='tagslist'),
    path(r'filterednotes/<id_tag>', views.filteredNotes, name='filterednotes')
]