from django.urls import path
from tasks.views import home, search, tags, tag_list


urlpatterns = [

    path('', search, name='search'),
    path('tags/', tags, name='tags'),
    path('tag_list/<str:tag>', tag_list, name='tag_list')
]