import os
import random

from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from OnlineBookStore.utils import unique_slug_generator


class BookCustomQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(book_active=True)

    def featured(self):
        return self.filter(book_featured=True, active=True)


class BookManager(models.Manager):

    def get_queryset(self):
        return BookCustomQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id1):
        qs = self.get_queryset().filter(book_id=id1, book_active=True)
        if qs:
            return qs.first()
        return None


def upload_image_path(instance, filename):
    random_folder_name = random.randint(1, 126871632781832)
    random_file_name = "{}{}".format(random_folder_name, os.path.splitext(os.path.basename(filename))[1])
    return os.path.join("books", str(random_folder_name), random_file_name)


def upload_image_single_path(instance, filename):
    random_folder_name = random.randint(1, 126871632781832)
    random_file_name = "{}{}".format(random_folder_name, os.path.splitext(os.path.basename(filename))[1])
    return os.path.join("singleproduct", str(random_folder_name), random_file_name)


# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(error_messages={'required': 'book id is required'}, null=False,
                               blank=False,
                               primary_key=True, db_column='book_id', verbose_name='book id',
                               help_text="primary key of book table",
                               unique=True)

    book_title = models.CharField(unique=True, default="Title", help_text="title of the book",
                                  verbose_name="Title",
                                  db_column="book_title", blank=False, null=False,
                                  error_messages={'required': 'book title is required'}, max_length=100,
                                  )
    book_isbn = models.IntegerField(unique=True, default="1234567890", help_text="Book ISBN number",
                                    verbose_name="ISBN",
                                    db_column="book_isbn", blank=False, null=False,
                                    error_messages={'required': 'book isbn is required'},
                                    )
    book_description = models.CharField(default="Description of the book", max_length=500,
                                        error_messages={'required': 'book Description is required'},
                                        null=False,
                                        blank=False, db_column="book_description",
                                        help_text="Description of the book",
                                        verbose_name="book description")
    book_price = models.DecimalField(verbose_name="Book price", help_text="price of the book",
                                     blank=False,
                                     null=False, default=0.00, max_digits=10, decimal_places=2,
                                     db_column='book_price',
                                     error_messages={'required': 'book Price is required'}, )
    book_price_new = models.DecimalField(verbose_name="Book price New", help_text="New price of the book",
                                         blank=False,
                                         null=False, default=0.00, max_digits=10, decimal_places=2,
                                         db_column='book_price_new',
                                         error_messages={'required': 'New book Price is required'}, )
    book_image = models.ImageField(verbose_name="image name", null=False, blank=False,
                                   help_text="image of the book", db_column='book_image',
                                   error_messages={'required': 'please upload book image'},
                                   default="default.jpg", upload_to=upload_image_path)
    book_image_single = models.ImageField(verbose_name="Individual Image", null=False, blank=False,
                                          help_text="Individual Image of the book", db_column='book_image_individual',
                                          error_messages={'required': 'please upload individual book image'},
                                          default="default.jpg", upload_to=upload_image_single_path)

    book_slug = models.SlugField(null=True, blank=True, help_text="Book slug field", db_column="book_slug",
                                 verbose_name="slug book", error_messages={"required": "Enter the Book slug field"},
                                 unique=True, )

    book_featured = models.BooleanField(default=False, db_column='book_featured', null=True, blank=True,
                                        help_text="Featured book or not ", verbose_name="Featured Book",
                                        error_messages={"required": "Book Featured required"})
    book_best_seller = models.BooleanField(default=False, db_column='book_best_seller', null=True, blank=True,
                                           help_text="book best seller or not ", verbose_name="book best seller",
                                           error_messages={"required": "book best seller status"})
    book_new_arrival = models.BooleanField(default=False, db_column='book_new_arrival', null=True, blank=True,
                                           help_text="book_new_arrival or not ", verbose_name="book new arrival",
                                           error_messages={"required": "book new arrival status"})
    book_active = models.BooleanField(default=False, db_column='book_active', null=True, blank=True,
                                      help_text="book status is active or not", verbose_name="Featured Active",
                                      error_messages={"required": "Book status"})
    book_stock = models.BooleanField(default=False, db_column='book_stock', null=True, blank=True,
                                     help_text="book is in stock or not", verbose_name="Book stock",
                                     error_messages={"required": "Book Stock Status"})

    book_rating = models.CharField(default=1, db_column='book_rating', null=True, blank=True,
                                   help_text="book rating in 5 ", verbose_name="Book Rating",
                                   error_messages={"required": "Book Rating"}, max_length=5)

    book_related = models.ManyToManyField(to='self', verbose_name='Related books',
                                          help_text="Related books", null=True, blank=True,
                                          error_messages={"required": "Related Books"}, db_column="book_related",
                                          )

    objects = BookManager()

    class Meta:
        db_table = 'books'
        verbose_name = 'books'
        verbose_name_plural = 'books'
        default_manager_name = 'objects'

    def __str__(self):
        return self.book_title

    def __unicode__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse('books:individual-book', kwargs={'book_slug': self.book_slug, 'book_isbn': self.book_isbn})

    @property
    def name(self):
        return self.book_title


def books_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.book_slug:
        instance.book_slug = unique_slug_generator(sender, instance, *args, **kwargs)


pre_save.connect(books_pre_save_receiver, sender=Books)
