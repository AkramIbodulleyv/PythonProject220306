from django.urls import path
from .views import (BookListView,
                    BookDetailView,
                    AllBookListView,)

urlpatterns = [
     path('', BookListView.as_view(), name='home'),
     path('all_books/', AllBookListView.as_view(), name='all_books'),
     path('book_detail/<int:pk>/', BookDetailView.as_view(), name='books-detail'),
 ]