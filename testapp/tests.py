from django.test import TestCase
from django.urls import reverse
from testapp.models import Book
from datetime import datetime, timedelta
from testapp.models import Bus

# Create your tests here.
class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Author Name", borrow_count=101,
                            published_date=datetime.now().date() - timedelta(days=30))
        Book.objects.create(title="Another Test Book", author="Another Author", borrow_count=50,
                            published_date=datetime.now().date() - timedelta(days=800))

    def test_is_popular(self):
        popular_book = Book.objects.get(title="Test Book")
        not_popular_book = Book.objects.get(title="Another Test Book")

        self.assertTrue(popular_book.is_popular())
        self.assertFalse(not_popular_book.is_popular())

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")

        self.assertEqual(book.author, second="Author Name")
        self.assertEqual(book.borrow_count, 101)

    def test_genre(self):
        book = Book.objects.get(title="Test Book")
        book.genre = "Fantasy"
        book.save()
        self.assertEqual(book.genre, "Fantasy")

    def test_string_representation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.string_representation(),
            "Test Book by Author Name")

    def  test_get_absolute_url(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.get_absolute_url(), reverse('book-detail', kwargs={
            'pk': book.pk}))

    def test_available_default(self):
        book = Book.objects.get(title="Test Book")
        self.assertTrue(book.available)

    def test_reserve_method(self):
        book = Book.objects.get(title="Test Book")
        book.reserve()
        self.assertFalse(book.available)

    def test_is_new_release(self):
        new_release_book = Book.objects.get(title="Test Book")
        self.assertTrue(new_release_book.is_new_release())
        not_new_release_book = Book


class BusTest(TestCase):
    def setUp(self):
        Bus.objects.create(nameBus="Test Bus",
                           content="to jest autobus",
                            popular=2,
                           year = 2020,
                           price = 150
                           )

        Bus.objects.create(nameBus="Another Test Bus",
                           content="to jest autobus",
                           popular=1,
                           year=2010,
                           price=90
                           )

    def test_is_popular(self):
        popular_bus = Bus.objects.get(nameBus="Test Bus")
        self.assertTrue(popular_bus.is_popular())

    def test_is_new(self):
        bus = Bus.objects.get(nameBus="Test Bus")
        busisolder = Bus.objects.get(nameBus="Another Test Bus")

        self.assertTrue(bus.is_new())
        self.assertFalse(busisolder.is_new())

    def test_is_expensive(self):
        busexpensive = Bus.objects.get(nameBus="Test Bus")
        buscheap = Bus.objects.get(nameBus="Another Test Bus")

        self.assertTrue(busexpensive.is_expensive())
        self.assertFalse(buscheap.is_expensive())
