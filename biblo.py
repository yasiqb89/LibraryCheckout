import datetime
import warnings
import sys


class MaxBooksLimitError(Exception):
    pass


class LibraryCheckout:
    def __init__(self):
        self.checked_out_books = []
        self.available_books = [
            "The Hobbit", "1984", "To Kill a Mockingbird", "Moby Dick", "Pride and Prejudice"
        ]
        self.is_valid_member = False
        self.late_fee_rate = 1.50  # $1.50 per day

    def checkout_book(self, book_title):
        if len(self.checked_out_books) >= 3:
            raise MaxBooksLimitError("You cannot check out more than 3 books at a time.")
        if book_title not in self.available_books:
            warnings.warn("This book is not available in our catalog.", UserWarning)
        else:
            self.checked_out_books.append(book_title)
            return f"Successfully checked out {book_title}!"

    def validate_membership(self):
        """Supposed to set self.is_valid_member to True, but it has a bug."""
        self.is_valid_member = False  # Bug: Should be True

    def calculate_late_fee(self, overdue_days):
        return overdue_days * self.late_fee_rate

    def renew_book(self, book_title):
        """Renewing books is currently not working correctly."""
        return False  # Bug: Should renew the book, but always returns False
