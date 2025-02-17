import biblo
import unittest
import sys

class TestBiblo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Starting Library Checkout Tests...")

    def setUp(self):
        self.biblo = biblo.LibraryCheckout()

    def tearDown(self):
        self.biblo = None

    #Test single book checkout
    def test_basic_checkout_book(self):
        message = self.biblo.checkout_book("The Hobbit")
        self.assertEqual(message, "Successfully checked out The Hobbit!")

    #Test multiple book checkout
    def test_multiple_checkout_book(self):
        self.books = ["1984", "To Kill a Mockingbird", "Moby Dick"]
        for book in self.books:
            with self.subTest(book = book):
                message = self.biblo.checkout_book(book)
                self.assertEqual(message, f"Successfully checked out {book}!")
                self.biblo = biblo.LibraryCheckout()

    @unittest.skip
    def test_maximum_checkout_book(self):
        books = ["1984", "To Kill a Mockingbird", "Moby Dick"]
        for book in books:
            self.biblo.checkout_book(book)  # Checkout 3 books

        # Attempt to check out the 4th book using subTest
        with self.assertRaises(biblo.MaxBooksLimitError):
            self.biblo.checkout_book("Pride and Prejudice")

    def test_checkout_book_available(self):
        self.assertIn("Pride and Prejudice", self.biblo.available_books)

    @unittest.expectedFailure
    def test_validate_membership(self):
        self.assertTrue(self.biblo.is_valid_member)

    @unittest.skipUnless(sys.version_info >= (3,8), "Python version")
    def test_calculate_late_fee(self):
        with self.assertWarns(UserWarning):  # Start monitoring for a warning
            self.biblo.checkout_book("A Nonexistent Book")  # This should trigger a warning

    @unittest.expectedFailure
    def test_renew_book(self):
        self.assertTrue(self.biblo.renew_book("Spider-man"))



if __name__ == '__main__':
    unittest.main()