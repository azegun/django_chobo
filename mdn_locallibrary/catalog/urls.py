from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/[NoReverseMatch]<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('author/[NoReverseMatch]<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]