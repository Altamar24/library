from django.http import JsonResponse

from .models import Book


def index(requset):
    queryset = Book.objects.all()
    books = [
        {
            'book.title': book.title,
            'book.year': book.year,
            'book.author': book.author.__str__(),
        } for book in queryset
    ]
    return JsonResponse({'books': books})
