
from book.views import ListBook,NewBook,BookDetail,EditBook
from django.urls import path


urlpatterns = [
    path('', ListBook.as_view(), name='list'),
    path('add/', NewBook.as_view(), name='add'),
    path('bookDetail/<int:pk>/', BookDetail.as_view(),name='bookDetail'),
    path('edit/<int:pk>/', EditBook.as_view(), name='edit'),
]