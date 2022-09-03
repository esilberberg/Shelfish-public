from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('books/', views.books_list, name='books'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('author/<int:author_id>', views.author_detail, name='author_detail'),
    path('classification/', views.classification_list, name='classification'),
    path('classification/<int:classification_id>', views.classification_detail, name='classification_detail'),
    path('classification/lang/<int:language_id>', views.language_detail, name='language_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('search_books/', views.search_books, name='search_books'),
]