from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import (CreateAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView, )

from .models import Books
from .serializers import BookSerializer


class BookListView(ListAPIView):
    queryset = Books.objects.all()
    lookup_field = 'book_slug'
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('book_slug', 'book_featured', 'book_id')
    search_fields = ('book_slug', 'book_featured', 'book_id')


class RetrieveBookView(RetrieveAPIView):
    queryset = Books.objects.all()
    lookup_field = 'book_slug'
    serializer_class = BookSerializer


class AddBookView(CreateAPIView):
    lookup_field = 'book_slug'
    serializer_class = BookSerializer


class DeleteBookView(DestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = 'book_slug'


class UpdateBookView(UpdateAPIView):
    queryset = Books.objects.all()
    lookup_field = 'book_slug'
    serializer_class = BookSerializer
