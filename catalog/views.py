from urllib import response
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import AddBook, AddAuthor
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages

def index(request):
    books = Book.objects.all().order_by('-date_created')[0:12]
    context = {
        'books': books,
    }
    return render(request, 'index.html', context=context)

def about(request):
    num_books = Book.objects.all().count()
    context = {
        'num_books': num_books,
    }

    return render(request, 'catalog/about.html', context=context)

def books_list(request): 
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'catalog/book_detail.html', {'book': book})

def add_book(request): 
    submitted = False
    if request.method == "POST":
        book_form = AddBook(request.POST)
        author_form = AddAuthor(request.POST)

        if book_form.is_valid() and author_form.is_valid():
            author = author_form.save()
            book = book_form.save(commit=False)

            book.author = author
            book.save()
            # save_m2m is required on form (book_form) not object (book) if commit=False is called
            book_form.save_m2m()

            return HttpResponseRedirect('/add_book?submitted=True')     
    else: 
        book_form = AddBook
        author_form = AddAuthor
        if 'submitted' in request.GET:
            submitted = True  
    
    context = {
        'book_form': book_form,
        'author_form': author_form,
        'submitted': submitted,
    }

    return render(request, 'catalog/add_book.html', context=context)

def search_books(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched == '':
            messages.success(request, ("You registered an empty search."))
            return redirect('catalog:index')
        else:
            for term in searched.split():
                books = Book.objects.filter(Q(title__icontains=term) |
                                            Q(publisher__icontains=term) |
                                            Q(summary__icontains=term) |
                                            Q(pub_year__icontains=term) |
                                            Q(author__first_name__icontains=term) |
                                            Q(author__surname__icontains=term) |
                                            Q(classification__term__icontains=term) |
                                            Q(language__name__icontains=term))
                books = books.distinct()
                result_count = books.count
            context = {
                'searched': searched,
                'books': books,
                'result_count': result_count,
            }
            return render(request, 'catalog/search_books.html', context=context)
    else:
        return render(request, 'catalog/search_books.html', {})

def classification_list(request):
    content = Classification.objects.filter(Q(term='Fiction') | Q(term='Non-Fiction')).order_by('term')
    classification = Classification.objects.all()
    geography = classification[2:7]
    language = Language.objects.all()
    subject = classification[7:]

    context = {
        'classification': classification,
        'language': language,
        'content': content,
        'geography': geography,
        'subject': subject,
    }
    return render (request, 'catalog/classification_list.html', context=context)

def classification_detail(request, classification_id):
    classification = get_object_or_404(Classification, pk=classification_id)
    books = Book.objects.filter(classification=classification)

    context = {
        'classification': classification,
        'books': books,
    }
    return render(request, 'catalog/classification_detail.html', context=context)

def language_detail(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    books = Book.objects.filter(language=language)

    context = {
        'language': language,
        'books': books,
    }
    return render(request, 'catalog/language_detail.html', context=context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)

    books = books.order_by('-pub_year')
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'catalog/author_detail.html', context=context)