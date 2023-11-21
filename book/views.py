from django.urls import reverse_lazy
from django.views import View
from book.forms import BookForm
from book.models import Book
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
"""
class ListBook(View):
    def get(self,request):
        books = Book.objects.all()
        return render(request, 'book/list.html', {'books': books})

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
"""

class ListBook(ListView):
    model= Book
    template_name = 'book/list.html'

class BookDetail(DetailView):
    model= Book
    template_name = 'book/bookDetail.html'

class EditBook(UpdateView):
    model = Book
    fields = ["title", "author","rating","sinopsys"]
    template_name = "book/editBook.html"
    success_url = reverse_lazy('list')

class DeleteBook(DeleteView):
    model = Book
    template_name = "book/book_check_delete.html2   "
    success_url = reverse_lazy("list")


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

