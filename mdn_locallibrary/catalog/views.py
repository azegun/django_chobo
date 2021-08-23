from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic

from catalog.models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_money = Book.objects.filter(title__exact='돈')
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_money': num_money,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'  # html에서 맞혀줘야함
    queryset = Book.objects.all()[:]  # 소문자 대문자 가리자 않는다는 뜻.
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    print("queryset>> ", queryset)


class AuthorList(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'author_list'
    queryset = Author.objects.all()
    template_name = 'catalog/author_list.html'
    print("queryset>> ", queryset)


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})

        # try:
        #     book = Book.objects.get(pk=primary_key)
        # except Book.DoesNotExist:
        #     raise Http404('책이 없습니다.')
        # return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorDetailView(generic.DetailView):
    model = Author

    def book_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})
