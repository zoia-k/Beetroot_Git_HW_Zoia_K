# Task 1
'''
Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
and make their own implementation of the method talk be different.
For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
and performs talk method on input parameter.
'''


class Animal:

    def talk(self):
        pass


class Dog(Animal):

    def talk(self):
        print('Woof! Woof!')


class Cat(Animal):

    def talk(self):
        print('Meow!')


def animal_talks(animal):
    animal.talk()


cat = Cat()
dog = Dog()

animal_talks(cat)
animal_talks(dog)

# Task 2
'''
Library

Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class
Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and 
        adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
'''


class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __repr__(self):
        return f'Author: {self.name}, {self.country}, {self.birthday}'


class Book:
    counter = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.counter += 1

    def __str__(self):
        return f"'{self.name}' by {self.author.name}, {self.year}"

    def __repr__(self):
        return f"Book: '{self.name}', written by {self.author.name} in {self.year}"


class Library:

    def __init__(self, name, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = authors

    def __str__(self):
        return f'{self.name},{self.books}, {self.authors}'

    def __repr__(self):
        return f'{self.name},{self.books}, {self.authors}'

    def new_book(self, name: str, year: int, author: Author) -> Book:
        book = Book(name, year, author)
        author.books.append(book)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        author_sorted_books = []
        for book in self.books:
            if book.author.name == author:
                author_sorted_books.append(book)
        return author_sorted_books

    def group_by_year(self, year: int):
        year_sorted_books = []
        for book in self.books:
            if book.year == year:
                year_sorted_books.append(book)
        return year_sorted_books


library = Library('School Library')
author_1 = Author('Stiven King', 'USA', '21/09/1947')

print(library.new_book('Christine', 1983, author_1))
print(library.new_book('The Girl Who Loved Tom Gordon', 1999, author_1))
print(Book.counter)
print(library)
print(library.group_by_author('Stiven King'))
print(library.group_by_year(1983))
print(library.group_by_year(1999))


# Task 3

# Fraction

# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
# з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій
# та операції порівняння між об'єктами класу Fraction
import math


class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be 0! Division on 0 is impossible')
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        com_denominator = self.lsm(self.denominator, other.denominator)
        new_numerator = self.numerator * com_denominator // self.denominator + other.numerator * com_denominator // other.denominator
        return self.normalized(new_numerator, com_denominator)

    def __sub__(self, other):
        com_denominator = self.lsm(self.denominator, other.denominator)
        new_numerator = self.numerator * com_denominator // self.denominator - other.numerator * com_denominator // other.denominator
        return self.normalized(new_numerator, com_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return self.normalized(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError('Denominator cannot be 0! Division on 0 is impossible')
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return self.normalized(new_numerator, new_denominator)

    def lsm(self, numerator, denominator):
        return (numerator * denominator) // math.gcd(numerator, denominator)

    def normalized(self, numerator, denominator):
        multiplicity = math.gcd(numerator, denominator)
        return Fraction(numerator // multiplicity, denominator // multiplicity)

    def __eq__(self, other):
        a = self.normalized(self.numerator, self.denominator)
        b = self.normalized(other.numerator, other.denominator)
        return a.numerator == b.numerator and a.denominator == b.denominator


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    assert x + y == Fraction(3, 4)
    assert x - y == Fraction(1, 4)
    assert x * y == Fraction(1, 8)
    assert x / y == Fraction(2, 1)
