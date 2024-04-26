class Author:
    def __init__(self, name):
        self.name = name
        self.author_contracts = []
        self.author_books = []

    def contracts(self):
        return self.author_contracts

    def books(self):
        return self.author_books
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        self.author_contracts.append(new_contract)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.author_contracts)
    


    



class Book:
    def __init__(self, title):
        self.title = title
        self.book_contracts = []

    def contracts(self):
        return self.book_contracts

    def authors(self):
        return [contract.author for contract in self.book_contracts]

        



class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        
        if not isinstance(author, Author):
            raise Exception("Invalid author object provided.")
        if not isinstance(book, Book):
            raise Exception("Invalid book object provided.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]