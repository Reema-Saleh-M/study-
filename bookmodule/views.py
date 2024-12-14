from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, 'bookmodule/index.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})

def viewbook(request, bookId):
    book = Book.objects.get(id=bookId)
    return render(request, 'bookmodule/one_book.html', {'book': book})

def links_page(request):
    return render(request, 'bookmodule/links.html')

def search_books(request):
    if request.method == "POST":
        # Get data from the form
        keyword = request.POST.get('keyword', '').lower()
        is_title = request.POST.get('option1')
        is_author = request.POST.get('option2')

        # Start with an empty queryset
        books = Book.objects.none()

        # Search logic
        if is_title and is_author:
            books = Book.objects.filter(title__icontains=keyword) | Book.objects.filter(author__icontains=keyword)
        elif is_title:
            books = Book.objects.filter(title__icontains=keyword)
        elif is_author:
            books = Book.objects.filter(author__icontains=keyword)

        # Render the results page with filtered books
        return render(request, 'bookmodule/bookList.html', {'books': books})

    # Render the form page for GET requests (when the form is just displayed)
    return render(request, 'bookmodule/search.html')
    
    def insert_books():
        Book.objects.create(
        title="Continuous Delivery",
        author="J. Humble and D. Farley",
        price=120.00,
        edition=3,
        description="A book on continuous delivery practices.",
        published_date="2010-09-10",
        isbn="9780321601919"
    )
    Book.objects.create(
        title="Reversing: Secrets of Reverse Engineering",
        author="E. Eilam",
        price=97.00,
        edition=2,
        description="A guide to reverse engineering techniques.",
        published_date="2005-01-01",
        isbn="9780596006707"
    )
    Book.objects.create(
        title="The Hundred-Page Machine Learning Book",
        author="Andriy Burkov",
        price=100.00,
        edition=4,
        description="A compact guide to machine learning.",
        published_date="2019-07-01",
        isbn="9781999643309"
    )
    Book.objects.create(
        title="Clean Code",
        author="Robert C. Martin",
        price=55.00,
        edition=2,
        description="A book about writing clean, maintainable code.",
        published_date="2008-08-11",
        isbn="9780132350884"
    )
    Book.objects.create(
        title="Design Patterns: Elements of Reusable Object-Oriented Software",
        author="Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        price=75.00,
        edition=1,
        description="Classic software design patterns book.",
        published_date="1994-10-21",
        isbn="9780201633610"
    )
    Book.objects.create(
        title="The Pragmatic Programmer",
        author="Andrew Hunt and David Thomas",
        price=50.00,
        edition=2,
        description="A guide to becoming a better programmer.",
        published_date="1999-10-20",
        isbn="9780201616224"
    )
    Book.objects.create(
        title="The Mythical Man-Month",
        author="Fred Brooks",
        price=60.00,
        edition=1,
        description="A book on software engineering and project management.",
        published_date="1975-11-01",
        isbn="9780201835953"
    )
    Book.objects.create(
        title="Introduction to Algorithms",
        author="Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        price=150.00,
        edition=3,
        description="Comprehensive textbook on algorithms.",
        published_date="2009-07-31",
        isbn="9780262033848"
    )
    Book.objects.create(
        title="Refactoring: Improving the Design of Existing Code",
        author="Martin Fowler",
        price=45.00,
        edition=2,
        description="A book on improving code structure through refactoring.",
        published_date="2018-12-18",
        isbn="9780134757599"
    )
    Book.objects.create(
        title="The Clean Coder: A Code of Conduct for Professional Programmers",
        author="Robert C. Martin",
        price=40.00,
        edition=1,
        description="A guide to professionalism in coding.",
        published_date="2011-05-01",
        isbn="9780137081073")


