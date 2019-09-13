import requests
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status


def home(request):
    if request.method == "GET":
        book_list = requests.get('http://localhost:8000/api/v1/lb').json()
        final_book_list = []
        for book in book_list:
            book['r'] = range(int(book['book_rating']))
            book['n'] = range(5 - int(book['book_rating']))
            final_book_list.append(book)
        context = {
                'book_list': final_book_list
        }
        return render(request, 'home.html', context=context)

    return render(request, '404.html', context={'error': "Method not allowed"})


def single_book_modal(request, book_slug):
    csrf_token = request.COOKIES['csrftoken']
    book = requests.get('http://localhost:8000/api/v1/{}/rb'.format(book_slug)).json()
    book_slug = book['book_slug']
    book_image = book['book_image']
    book_price = book['book_price']
    book_description = book['book_description']
    book_title = book['book_title']
    if request.method == "GET":
        dynamic_html = """
                        <div class="modal fade" id="productModal" tabindex="-1" role="dialog">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                                                aria-hidden="true">&times;</span></button>
                                    </div>
                                    <div class="modal-body">
                                        <div class="modal-product">
                                            <div class="product-images">
                                                <div class="main-image images">
                                                    <img alt=" slug? log " src="img?">
                                                </div>
                                            </div>
                                            <div class="product-info">
                                                <h1>title?</h1>
                                                <div class="price-box">
                                                    <p class="s-price"><span class="special-price"><span
                                                            class="amount">$ price?</span></span></p>
                                                </div>
                                                <a href="#" class="see-all">See all features</a>
                                                <div class="quick-add-to-cart">
                                                    <form method="post" class="cart" action="#">
                                                         <input name="csrfmiddlewaretoken" type="hidden" value="csrf_token?">
                                                        <div class="numbers-row">
                                                            <label for="french-hens"></label><input type="number" id="french-hens"
                                                                                                    value="1">
                                                        </div>
                                                        <button class="single_add_to_cart_button" type="button">Add to cart</button>
                                                    </form>
                                                </div>
                                                <div class="quick-desc">
                                                    desc?
                                                </div>
                                                <div class="social-sharing">
                                                    <div class="widget widget_socialsharing_widget">
                                                        <h3 class="widget-title-modal">Share this product</h3>
                                                        <ul class="social-icons">
                                                            <li><a target="_blank" title="Facebook" href="#" class="facebook social-icon"><i
                                                                    class="fa fa-facebook"></i></a></li>
                                                            <li><a target="_blank" title="Twitter" href="#" class="twitter social-icon"><i
                                                                    class="fa fa-twitter"></i></a></li>
                                                            <li><a target="_blank" title="Pinterest" href="#" class="pinterest social-icon"><i
                                                                    class="fa fa-pinterest"></i></a></li>
                                                            <li><a target="_blank" title="Google +" href="#" class="gplus social-icon"><i
                                                                    class="fa fa-google-plus"></i></a></li>
                                                            <li><a target="_blank" title="LinkedIn" href="#" class="linkedin social-icon"><i
                                                                    class="fa fa-linkedin"></i></a></li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- .product-info -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>"""
        msg = dynamic_html.replace('title?', book_title).replace('desc?', book_description) \
            .replace('img?', book_image).replace('slug?', book_slug).replace('price?', book_price) \
            .replace('csrf_token?', csrf_token)

        return JsonResponse(data=msg, status=status.HTTP_200_OK, safe=False)
    return render(request, '404.html')


def featured_book(request):
    if request.method == "GET":
        book_list = requests.get('http://localhost:8000/api/v1/lb/?book_featured=true').json()
        context = {
                'book_list': book_list
        }
        return render(request, 'featured.html', context=context)

    return render(request, '404.html', context={'error': "Method not allowed"})


def individual_book(request, book_slug, book_isbn):
    final_related_book_list = []
    if request.method == "GET":
        book = requests.get('http://localhost:8000/api/v1/{}/rb/'.format(book_slug)).json()
        context = {
                'book': book,
                'r': range(int(book['book_rating'])),
                'n': range(5 - int(book['book_rating']))
        }
        for b in book['book_related']:
            related_book_dict = {}
            related_book = requests.get('http://localhost:8000/api/v1/lb/?book_id={}'.format(b)).json()[0]
            related_book_dict['r'] = range(int(related_book['book_rating']))
            related_book_dict['n'] = range(5 - int(related_book['book_rating']))
            related_book_dict['b'] = related_book
            final_related_book_list.append(related_book_dict)
        context['related_book'] = final_related_book_list
        return render(request, 'book_detail.html', context=context)

    return render(request, '404.html', context={'error': "Method not allowed"})


def wishlist(request):
    context = {}
    return render(request, 'wishlist.html', context=context)


def shop(request):
    if request.method == "GET":
        final_book_list = []
        book_list = requests.get('http://localhost:8000/api/v1/lb').json()
        for book in book_list:
            book['r'] = range(int(book['book_rating']))
            book['n'] = range(5 - int(book['book_rating']))
            final_book_list.append(book)
        context = {'book_list': final_book_list}
        return render(request, 'shop.html', context=context)

    return render(request, '404.html', context={'error': "Method not allowed"})
