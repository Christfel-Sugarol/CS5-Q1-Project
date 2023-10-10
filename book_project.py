import time

class book:
    def __init__(self,title,author,year,status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def getAllValues(self):
        return [self.title, self.author, self.year,self.status]    
    


books = []

def searchByPara(para, mode, num = 0, book_list = []):
    if num == len(books):
        if len(book_list) == 0:
            print("No books fitting the criteria exist")
            return None

        for i in book_list:
            book_status = ""
            if i.getAllValues()[3] == True:
                book_status = "Available"
            else:
                book_status = "Checked out"    


            print("Title: {} || Author: {} || Year of Publication: {} || Status: {}".format(i.getAllValues()[0], i.getAllValues()[1], i.getAllValues()[2], book_status))
        

        for i in reversed(book_list):
            book_list.remove(i)
        return None


    if books[num].getAllValues()[mode] == para:
        book_list.append(books[num])


    return searchByPara(para, mode, num+1, book_list)



def searchByTitle(title):
    for i in books:
        if i.title == title:
            return i
    return False

def add_book():
    print("Currrently adding a book...")
    title = raw_input("Enter the title: ")
    author = raw_input("Enter the author: ")
    
    year = ""

    while True:
        year = raw_input("Enter the year of publiction: ")
        if year.isdigit():
            break

    status = True

    books.append(book(title, author, year, status))

def checkout_book():
    print("Currently checking out a book...")
    user_input = raw_input("Enter the title: ")

    if(not searchByTitle(user_input)):
        print("not in library")

    elif (searchByTitle(user_input).status == True):
        searchByTitle(user_input).status = False
        print("successfully checked out")
              
    else:
        print("Book has been already checked out")

def return_book():
    print("Currently returning a book...")
    user_input = raw_input("Enter the title: ")

    if(not searchByTitle(user_input)):
        print("not in library")

    elif (searchByTitle(user_input).status == False):
        searchByTitle(user_input).status = True
        print("Successfully returned")
              
    else:
        print("Book is already in library")

def intro():
    time.sleep(0.5)
    print("")
    print("-------------------------------------")
    print("1. Add a book")
    print("2. Check out a book")
    print("3. Return a book")
    print("4. Search books by author")
    print("5. Search books by year of publication")
    print("6. Check books by status")
    print("7. Exit ")

while True:
    choice = ""

    intro()

    while True:
        print("-------------------------------------")
        choice = raw_input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)

            if (choice >= 1) and (choice <= 7):
                break
            else:
                print("Enter a number within 1 to 7!!!")
        else:
            print("Enter a valid number!!!")

    choice = int(choice)


    if choice == 1:
        add_book()
    elif choice == 2:
        checkout_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        searchByPara(raw_input("Enter the name of the author: "), 1)
    elif choice == 5:
        while True:
            year = raw_input("Enter the year of publiction: ")
            if year.isdigit():
                break
            else:
                print("Enter a valid number!!!")

        searchByPara(year, 2)

    elif choice == 6:
        while True:
            book_status = raw_input("Enter the status of the book - available? (Y/N): ")

            if (book_status == "Y") or (book_status == "N" ):
                break
            else:
                "Enter either <Y> or <N>!!!"

        if book_status == "Y":
            book_status = True
        else:
            book_status = False            
        
        searchByPara(book_status, 3)
    else:
        break       








#print(searchByTitle("Alice in Wonderland"))     