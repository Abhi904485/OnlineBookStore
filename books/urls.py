from django.urls import path

from .api_views import BookListView, AddBookView, DeleteBookView, UpdateBookView, RetrieveBookView
from .views import (home, single_book_modal, featured_book, individual_book, wishlist, shop, )

app_name = 'books'
urlpatterns = [
        path('', home, name='home'),
        path('wishlist/', wishlist, name='wishlist'),
        path('shop/', shop, name='shop'),
        path('<str:book_slug>/single_book_modal/', single_book_modal, name='single_book'),
        path('featured_book/', featured_book, name='featured-book'),
        path('book/<str:book_slug>/<int:book_isbn>/', individual_book, name='individual-book'),
        path('api/v1/lb/', BookListView.as_view(), name='list-book'),
        path('api/v1/ab/', AddBookView.as_view(), name='add-book'),
        path('api/v1/<str:book_slug>/db/', DeleteBookView.as_view(), name='delete-book'),
        path('api/v1/<str:book_slug>/ub/', UpdateBookView.as_view(), name='update-book'),
        path('api/v1/<str:book_slug>/rb/', RetrieveBookView.as_view(), name='retrieve-book'),
]
