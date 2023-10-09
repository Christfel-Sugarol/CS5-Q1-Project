class book:
    def __init__(self,title,author,year,status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def getAllValues(self):
        return [self.title, self.author, self.year,self.status]    
    


books = []

def searchByKey(para, mode = 1, num = 0, book_list = []):
    #mode 0 = title
    #mode 1 = author
    #mode 2 = year of publication
    #mode 3 = status

    if num == len(books):
        return book_list

    if (books[num].getAllValues()[mode] == para):
        
        book_list.append(books[num].getAllValues())


    return searchByKey(para, mode, num+1, book_list)


#prints a given list of book with a predetermined format
def printListofBooks(book_list = []):
    for i in book_list:
        s_stat = ""
        if i[3] == True:
            s_stat = "Available"
        else: 
            s_stat = "Checked out"

        print("Title: {} || Author: {} || Year of Publication: {} || Status {} ".format(i[0], i[1], i[2], s_stat))

def searchByTitle(title):
    for i in books:
        if i.title == title:
            return i
    return False

#hazardous code, do not change

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


#fucking around area

add_book()
add_book()
add_book()

print(len(books))
printListofBooks(searchByKey("Balls", 1))

#print(searchByTitle("Alice in Wonderland"))            