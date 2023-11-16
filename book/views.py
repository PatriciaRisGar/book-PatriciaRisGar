from django.views import View
from book.forms import BookForm
from book.models import Book
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

class ListBook(View):
    def get(self,request):
        books = Book.objects.all()
        return render(request, 'book/list.html', {'books': books})


class NewBook(View):
    books = Book.objects.all()

    def post(self,request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
        return render(request, 'book/bookNew.html', {'books': self.books,'form': form})
    
    def get(self,request):
        form=BookForm()
        return render(request, 'book/bookNew.html', {'books': self.books,'form': form})

class BookDetail(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book/bookDetail.html', {'book': book})

class EditBook(View):

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST,instance=book)

        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'book/editBook.html', {'book': book, 'form': form})
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST,instance=book)
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book/editBook.html', {'book': book, 'form': form})

