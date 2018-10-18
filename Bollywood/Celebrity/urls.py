from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('home/', views.homeView, name='Home'),
    path('rest_operations/', views.RestOperations.as_view(), name='RestOperations'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
