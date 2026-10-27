class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.__isCheckOut = False

    def checkout(self):
        self.__isCheckOut = True
        print("Checked out successfully! ")

    def get_return_period(self):
        return 14

class Book(LibraryItem):
    def __init__(self, title):
        super().__init__(title)

    def get_return_period(self):
            return 21

class DVD(LibraryItem):
    def __init__(self, title):
        super().__init__(title)

    def get_return_period(self):
            return 7

book1 = Book("Time Chase")
book1.checkout()