from django.urls import path
from . import views
# from .views import HomeTemplateView

urlpatterns = [
    path('',views.index,name='index'),
    # path('',HomeTemplateView.as_view(),name='HomeTemplateView'),
]