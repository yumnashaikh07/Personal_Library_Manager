import json 
import os
import inquirer 

personal_library = "library_manager.txt"

def load_personal_library():
    if os.path.exists(personal_library):
        with open(personal_library, "r") as f:
            try:
                books = json.load(f)
            except json.JSONDecodeError:
                print("Error loading the library file! The file may be corrupted.")
                return {}  # Return empty dictionary if file content is invalid
        return books
    else:
        print("Library file not found! Creating a new one.")
        return {}

# Function  to save current state  
def save_personal_library(library):
    with open(personal_library , "w") as f:
        json.dump(library, f , indent = 3)  

def add_books(library):
    askedtitle = input("Enter Title of your book: ").strip().lower()
    askedauthor = input("Enter Author of your book: ").strip()   
    while True:
        askedyear = input("Enter Year of your book: ")
        if askedyear.isdigit() and 1000 <= int(askedyear) <= 2025:
            askedyear = int(askedyear)
            break
        else:
            print("❌ Invalid year! Please enter a valid number between 1000 and 2025.")
    askedgenre = input("Enter Genre of your book: ").strip()
    askedreading_status = input("Have you read this book or not? Y/N: ").strip().upper()
    if askedreading_status == "Y":
        askedreading_status = "Read"
    else:    
        askedreading_status = "Unread"
    if not askedtitle or not askedauthor or not askedyear or not askedgenre:
        print("❗Please fill all the fields correctly!")
        return
    else:
        added_book = {
            askedtitle: {
            "title": askedtitle, 
            "author": askedauthor, 
            "year": askedyear, 
            "genre": askedgenre, 
            "reading_status": askedreading_status}}
    library.update(added_book)
    print(f"✅Book '{askedtitle}' added successfully!")
    save_personal_library(library)  # all entered info given as argument here, in place of save_personal_library "library" parameter

def remove_book(library):
    removetitle = input("Enter Title of book to Remove: ").strip().lower()
    if removetitle in library:
        del library[removetitle]
        print(f"Book '{removetitle}' removed successfully!")
    else:
        print("Book not found in the library!")
    save_personal_library(library)

def view_books(library):
    if library :
        for _ in library:
            print(f"Title: {library[_]['title']} by {library[_]['author']} in {library[_]['year']} |{library[_]['genre']} \n {library[_]['reading_status']}")
    else:
        print("No books found in your library.")

def search_book(library):
    searchtitle = input("Enter Book Title to Search Book:").lower()
    if searchtitle in library:
        Searchedbook = library[searchtitle]
        print(f"Title: {Searchedbook['title']} by {Searchedbook['author']} in {Searchedbook['year']} |{Searchedbook['genre']} \n {Searchedbook['reading_status']}")
    else:
        print("Book not found in the library!")

library = load_personal_library()
while True:
    options = [inquirer.List("choices" , 
    message= "\n❓Select Any Option to get started" , 
    choices=[
        "1. Add Book",
        "2. Remove Book",
        "3. View All Books",
        "4. Search Book",
        "5. Exit",
    ])]
    user_choice = inquirer.prompt(options)
    choice = user_choice["choices"]
    if choice  == "1. Add Book":
        add_books(library)
    elif choice == "2. Remove Book":
        remove_book(library)
    elif choice == "3. View All Books":
        view_books(library)
    elif choice == "4. Search Book":
        search_book(library)
    elif choice == "5. Exit":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please try again.")