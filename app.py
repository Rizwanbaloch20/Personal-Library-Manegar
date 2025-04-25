import json
import os

data_file = 'data.json'

def load_data(file_path):
    """Load data from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_library(file_path, data):
    """Save library data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read,
    }

    library.append(new_book)
    save_library(data_file, library)
    print(f"Book '{title}' added to the library successfully.")

def remove_book(library):
    """Remove a book from the library."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(data_file, library)
            print(f"Book '{title}' removed from the library.")
            return
    print(f"Book '{title}' not found in the library.")

def view_books(library):
    """View all books in the library."""
    if not library:
        print("No books in the library.")
        return
    
    print("\nLibrary Books:")
    for book in library:
        read_status = "Read" if book["read"] else "Not Read"
        print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - {read_status}")

def search_books(library):
    """Search for books in the library."""
    search_term = input("Enter a title, author, or genre to search: ").lower()
    results = [book for book in library if (search_term in book["title"].lower() or 
                                            search_term in book["author"].lower() or 
                                            search_term in book["genre"].lower())]
    if not results:
        print("No matching books found.")
        return
    
    print("\nSearch Results:")
    for book in results:
        read_status = "Read" if book["read"] else "Not Read"
        print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - {read_status}")

def main():
    """Main function to run the library management system."""
    library = load_data(data_file)
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Search Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            view_books(library)
        elif choice == "4":
            search_books(library)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
