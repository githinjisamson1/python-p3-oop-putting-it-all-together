#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = title

        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    # getters
    def get_page_count(self):
        return self._page_count

    def get_title(self):
        return self._title

    # setters
    def set_page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    def set_title(self, title):
        self._title = title

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page_count, set_page_count)
    title = property(get_title, set_title)


book1 = Book("The Pearl", 200)
book1.turn_page()
# print(book1)
