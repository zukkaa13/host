from django.urls import path
from . import views
from .views import search_csv


urlpatterns = [
    path('', views.csv_view, name='csv-view'), 
    path('search/', search_csv, name='search_csv'),
    path('add_word/', views.add_word, name='add_word'),  # ახალი ვიუ დამატებისთვის

]
