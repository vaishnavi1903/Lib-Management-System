'''

book = {
    1 : {
        "Title" : "The Intelligent Investor",
        "Author" : "Benjamin Graham",
        "ISBN" : "TII-123BGTII",
        "Publisher" : "Harper Business"
    },
    2 : {
        "Title" : "The C Programming Language",
        "Author" : "Brian W. Kernighan and Dennis M. Ritchie",
        "ISBN" : "CPL-676BKDRCPL",
        "Publisher" : "Prentice Hall"
    },
    3 : {
        "Title" : "Rich Dad Poor Dad",
        "Author" : "Robert T. Kiyosaki",
        "ISBN" : "RDPD-2141RDPD",
        "Publisher" : "Plata Publishing"
    }
}

'''

book = {}


def add_book():
    print("\n")
    book_id = int(input("Enter the book number id:"))
    title = input("Enter the book title:")
    author = input("Enter the author name:")
    isbn = input("Enter the isbn number:")
    publisher = input("Enter the publisher's name:")
    
    book[book_id] = {"Title":title, "Author":author, "ISBN":isbn, "Publisher":publisher}
    print("\nBook added!\n\n")

def display_book():
    if len(book) == 0:
        print("\nNothing to display!")
    else:
        print("\n")
        for key, value in book.items():
            print("\n",key, end=" :")
            for k, v in value.items():
                print(" ' %s : %s '"%(k, v), end="\n   ")
            
def search_book():
    if len(book) == 0:
        print("\nNo books to search!")
    else:
        print("\n")
        book_id = int(input("Enter the book number id to search:"))
        if book_id in book:
            print("\nBook is present in the list")
        else:
            print("\nBook not found")

def delete_book():
    if len(book) == 0:
        print("\nNothing to delete!")
    else:
        print("\n")
        delete_id = int(input("Enter book id to delete: "))
        if delete_id not in book:
            print("\nNo book with this ID to delete!")
        else:
            del (book[delete_id])
            print("\nBook has been deleted!")
    
def clear_all():
    if len(book) == 0:
        print("\nRecords are already empty!")
    else:
        print("\n")
        book.clear()
        print("All records cleared\n")

def main():
    while(True):
        print("\n")
        print("\t\t  Library Management System\n\n")
        print("\t\t  1. Add a book")
        print("\t\t  2. Search a book")
        print("\t\t  3. Display all books")
        print("\t\t  4. Delete a specific book")
        print("\t\t  5. Clear all book list")
        print("\t\t  0. Exit\n")
        print("\t￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣\n")
        
        choice = input("\nEnter your choice:")
        if (choice == "1" or choice == "Add" or choice == "add"):
            add_book()
            
        elif (choice == "2" or choice == "Search" or choice == "choice"):
            search_book()
            
        elif (choice == "3" or choice == "Display" or choice == "display"):
            display_book()
            
        elif (choice == "4" or choice == "Delete" or choice == "delete"):
            delete_book()
            
        elif (choice == "5" or choice == "Clear" or choice == "clear"):
            clear_all()
        
        elif (choice == "0" or choice == "Exit" or choice == "exit"):
            exit(0)
            
        else:
            print("Enter a valid option!")
            break
            
main()