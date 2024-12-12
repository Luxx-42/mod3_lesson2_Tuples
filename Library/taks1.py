#Task 1 library system
def display_books(library):
    '''Display Books from the library'''
    display_all = input("Which book would you like to check on?" 
                        "(enter 'all' to print put the entire list): ")
    if display_all == 'all'.lower():
        for author, book_name in library:
            print(f"- Author: {author}, Book Name: {book_name}\n")
    
    else:
        found = False 
        for author, book_name in library:
            if display_all.lower() == author.lower() or display_all.lower() == book_name.lower():
                print(f"- Author: {author.capitalize()}, Book name:{book_name.capitalize()}")
                found = True
                break
                
        if not found:
            print("Book wasn't found.")


def add_books(library):
    '''Add books to the library'''
    add_author = input("enter the author's name: (first and last name): ").lower()
    book_name = input("\nEnter the name of the book: ")

    if (add_author, book_name) in library:
        print("This book is already in the library.")
        print("-" * 25)
    else:
        library.append((add_author, book_name))
        print("Your book was added to the library.")
        print("-" * 25)

def main():
    '''The main program'''
    library = [("George Orwell", "1984"), ("Aldous Huxley", "Brave New World")]

    while True:

        print("\n1. Display the list of library book.")
        print("2. Add a book to the list of books.")
        print("3. Exit Library.")
        print("-" * 25)
        your_choice = input("What would you like to do? ")

        if your_choice == '1':
            display_books(library)
        elif your_choice == '2':
            add_books(library)
        elif your_choice == '3':
            print("You have exited the library.")
            break
        else:
            print("Please enter in a number between 1-3.")

if __name__ == "__main__":
    main()