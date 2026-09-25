class book:
    def __init__(self, id_book, name, author, editorial):
        self.id = id_book
        self.name = name 
        self.author = author 
        self.editorial = editorial 
        self.avaliable = True 
    def show_book_info(self):
        return f"{self.id} - {self.name} - {self.author}"

class book:
    def __init__(self, id_book, name, author, editorial):
        self.id = id_book
        self.name = name
        self.author = author
        self.editorial = editorial
        self.avaliable = True  

    def show_book_info(self):
        status = "Disponible" if self.avaliable else "Prestado"
        return f"{self.id} - {self.name} - {self.author} [{status}]"