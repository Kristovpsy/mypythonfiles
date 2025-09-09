
library_books : dict = {
    "Animal Farm" : "George Orwell",
    "Dune" : "Frank Herbert",
    "Murder on the Orient express" : "Agatha Christie"

}

print("libarary collection :")


for book, author in library_books.items():
    print(f"'{book}' by {author}")

def display_books():
    if not library_books:
        print("the library is empty")
    else:
        print("library collection")
        
        for book, author in library_books.items():
             print(f"'{book}' by {author}")

def add_books():
     book = input(" enter book title:").strip()
     author = input(" enter author name:").strip()
     if book in library_books:
         print("book available")
     else:
         library_books[book] = author
         print(f"'{book}' by {author} has been added")
         display_books()


def remove_books():
    book = input("Enter book to remove").strip()
    if book in library_books:
        del library_books[book]
        print("book has been removed ")
        display_books()
    else:
        print("book not found")            

def search_books():
    book = input("Enter book You are looking for").strip()
    if book in library_books:
        print(f"found:'{book}' by {library_books[book]}")
    else:
        print("book not found")

while True: 
    print("\n----LIBRARY MENU----")
    print("1. Display a book")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Search a book")
    print("5. Exit")

    choice = input("choose an option(1-5):")
    if choice == "1":
        display_books()
    elif choice == "2":
        add_books()
    elif choice == "3":
        remove_books()
    elif choice == "4":
        search_books()
    elif choice == "5":
        print("Exit Library page. Goodbye!")

        break
    else:
        print("invalid choice")               
#abstraction
#encapulation

num : int = int(input("Enter a Number: "))
def number_to_words(num):
    units = ["zero","öne","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    if num < 20:
        return units[num]
    elif num < 100:
        return tens[num]
    elif num < 1000:
        return units [num//100]