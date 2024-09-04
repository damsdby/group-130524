from abc import ABC
from dataclasses import dataclass
from enum import Enum, unique, auto
from random import randint

from typing import Self


class LibraryItem(ABC):
    def __init__(self, title, author_or_director, year):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    def description(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author_or_director, year, number_of_pages):
        super().__init__(title, author_or_director, year)
        self.number_of_pages = number_of_pages

    def description(self):
        return f"Number of pages: {self.number_of_pages}"


class Magazine(LibraryItem):
    def __init__(self, title, author_or_director, year, issue_number=int):
        super().__init__(title, author_or_director, year)
        self.issue_number = issue_number

    def description(self):
        return f"year: {self.issue_number}"

class DVD(LibraryItem):
    def __init__(self, title, author_or_director, year, duration):
        super().__init__(title, author_or_director, year)
        self.duration = duration

    def description(self):
        return f"Duration: {self.duration} min"


book_one = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 223)
book_two = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 1998, 251)
magazine = Magazine("The Quibbler", "Xenophilius Lovegood", 2023, 10)
dvd = DVD("Harry Potter and the Deathly Hallows: Part 2", "David Yates", 2011, 130)

print(book_one.description())
print(book_two.description())
print(magazine.description())
print(dvd.description())
