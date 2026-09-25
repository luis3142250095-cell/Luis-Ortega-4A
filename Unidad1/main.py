from books import book 
from users import user
from library import library 

library1 = library()
#Instances:
book1 = book("001", "Python for dummies", "Juan Garcia", "Villarreal")
book2 = book("002", "OOP fundamentals", "Ana Sanchez", "E.A")
user1 = user("001", "Ricardo Rodriguez")

library1.add_book(book1)
library1.add_book(book2)
library1.add_users(user1)

library1.show_books()

#1. The system must allow to registrer books.
#2. The system must allow to registrer users.
#3. The system must allow a book to be borrowed by a user.
#4. A book that has already been borrowed cannot be borrowed again.
#5. The system must allow a book to be returned.


from books import book
from users import user
from library import library

library1 = library()

book1 = book("001", "Python for dummies", "Juan Garcia", "Villarreal")
book2 = book("002", "OOP fundamentals", "Ana Sanchez", "E.A")

library1.add_book(book1)
library1.add_book(book2)

user1 = user("001", "Ricardo Rodriguez")
library1.add_users(user1)

print("--- Estado inicial de libros ---")
library1.show_books()

print("\n--- Intento de préstamo 1 ---")
library1.borrow_book("001", "001")  # Presta 'Python for dummies' a Ricardo

print("\n--- Intento de préstamo 2 (libro no disponible) ---")
library1.borrow_book("001", "001")  # Intenta prestar el mismo libro de nuevo

print("\n--- Devolución de libro ---")
library1.return_book("001", "001")

print("\n--- Estado final de libros ---")
library1.show_books()