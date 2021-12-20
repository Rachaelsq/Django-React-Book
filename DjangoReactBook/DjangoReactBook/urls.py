#======================================
#PROJECT URLS
#======================================

#django imports
from django.contrib import admin
from django.urls import path
from django.forms import forms
from django import forms
#view imports
from bookapp.views import home_view
from bookapp.views import book_detail_view
from bookapp.views import book_create_view
from bookapp.views import books_list
#model imports
from bookapp.models import Books


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('bookapp/<int:book_id>', book_detail_view),
    path('create_book', book_create_view),
    path('books_list', books_list),
]