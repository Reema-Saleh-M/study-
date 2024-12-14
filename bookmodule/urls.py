from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.aboutus, name='aboutus'),
    path('books/', views.list_books, name='list_books'),
    path('book/<int:bookId>/', views.viewbook, name='viewbook'),  # <-- This is the important line
    path('links/', views.links_page, name='links_page'),
    path('search/', views.search_books, name='books.search'),

]

