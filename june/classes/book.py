class Book:
    count = 0

    def __init__(self, book_name):
        self.book_name = book_name
        Book.count  += 1

    @classmethod
    def book_count(cls):
        return cls.count
    
    @staticmethod
    def is_long(pages):
        if pages>100:
            return True
        return False

    