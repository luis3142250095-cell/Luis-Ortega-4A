class library:
    def __init__(self):
        self.books = []
        self.users = []

        def add_book(self, book):
            self.books.append(book)

        def add_users(self, user):
            self.users.append(user)

        def show_books(self):
            for book in self.books:
                print(book.show_book_info())

class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_users(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())

    def borrow_book(self, id_book, id_user):
        target_book = next((b for b in self.books if b.id == id_book), None)
        target_user = next((u for u in self.users if u.id == id_user), None)

        if not target_book:
            print(f"Error: El libro con ID '{id_book}' no existe.")
            return False
        if not target_user:
            print(f"Error: El usuario con ID '{id_user}' no existe.")
            return False

        if not target_book.avaliable:
            print(f"Error: El libro '{target_book.name}' ya se encuentra prestado.")
            return False

        target_book.avaliable = False
        target_user.borrowed_books.append(target_book)
        print(f"Éxito: El libro '{target_book.name}' ha sido prestado a {target_user.name}.")
        return True

    def return_book(self, id_book, id_user):
        target_book = next((b for b in self.books if b.id == id_book), None)
        target_user = next((u for u in self.users if u.id == id_user), None)

        if not target_book or not target_user:
            print("Error: Libro o usuario no encontrado.")
            return False

        if target_book in target_user.borrowed_books:
            target_book.avaliable = True
            target_user.borrowed_books.remove(target_book)
            print(f"Éxito: El libro '{target_book.name}' ha sido devuelto por {target_user.name}.")
            return True
        else:
            print(f"Error: El usuario {target_user.name} no tiene prestado el libro '{target_book.name}'.")
            return False