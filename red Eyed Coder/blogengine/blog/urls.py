from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts_list,name='posts_list_url'),
    path('post/<str:slug>/',views.post_detail,name='post_detail_url'),
    path('tags/',views.tags_list,name='tags_list_url'),
    path('tag/<str:slug>/',views.tag_detail,name='tag_detail_url'),
]