def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed")
    else:
        print(f"Book {book_id} cannot be borrowed.")
        
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned")
    else:
        print(f"Book {book_id} was not borrowed.")

def register_member(members, member_id):
    members.add(member_id)

def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"{book_id} -> {title}, {author}, {year}")

def main():
    
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 101, "Physic", "John", 2006)
    add_book(catalog, 102, "maths", "Alice", 2001)
    add_book(catalog, 103, "chemistry", "Andrew", 2000)
    add_book(catalog, 104, "Finance and Economics", "David", 1995)

    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)   

    print("Registered Members:", members)

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    print("Borrowed Books:", borrowed_books)

    return_book(borrowed_books, 101)

    print("Borrowed Books after return:", borrowed_books)

    show_available(catalog, borrowed_books)

main()