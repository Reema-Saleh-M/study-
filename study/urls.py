from django.contrib import admin
from django.urls import path
from bookmodule import views  # Ensure you're importing the views from the correct app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('books/', views.list_books, name='list_books'),  # Books listing page
    path('books/<int:bookId>/', views.viewbook, name='view_book'),  # View a specific book
    path('about/', views.aboutus, name='about_us'),  # About us page
    path('links/', views.links_page, name='links_page'),  # Links page
    path('', views.index, name='home'),  # Home page - root URL
    path('search/', views.search_books, name='books.search'),

]

