
###########################################################
# listofbooks will consist of the following information      #
#  title:     The book title                              #
#  isbn:      The ISBN number of a book                   #
#  author:    The author’s name                           #
#  publisher: The publisher’s name                        #
#  date:      The date the book was added to inventory    #
#  qty:       The quantity on hand of the book            #
#  wholesale: The wholesale cost of the book              #
#  retail:    The retail price of the book                #
###########################################################

############################
# Create a list named listofbooks.
#   Initialize the list to an empty list
#############################
from difflib import SequenceMatcher
import datetime
import time
import sys
from operator import itemgetter
listofbooks = []

###########################################################
#                                                         #
#  The bookInfo function displays the Book Information    #
#  Screen                                                 #
#                                                         #
###########################################################
class listofbooks:

    def __init__(self, title, isbn, author, publisher, date, qty, wholesale, retail):

        self.__title = title
        self.__isbn = isbn
        self.__author = author
        self.__publisher = publisher
        self.__date = date
        self.__qty = qty
        self.__wholesale = wholesale
        self.__retail = retail
       
    def set_title(self,title):
    ### DO THIS FOR EVERYONE OF EM####
        self.__title = title
    def get_title(self):
        return self.__title
    def set_isbn(self,isbn):
        self.__isbn = isbn
    def get_isbn(self):
        return self.__isbn
    def set_author(self,author):
        self.__author = author
    def get_author(self):
        return self.__author
    def set_publisher(self,publisher):
        self.__publisher = publisher
    def get_publisher(self):
        return self.__publisher
    def set_date(self,date):
        self.__date = date
    def get_date(self):
        return self.__date
    def set_qty(self,qty):
        self.__qty = qty
    def get_qty(self):
        return self.__qty
    def set_wholesale(self,wholesale):
        self.__wholesale = wholesale
    def get_wholesale(self):
        return self.__wholesale
    def set_retail(self,retail):
        self.__retail = retail
    def get_retail(self):
        return self.__retail

           
        
            
            
        

        
    def bookInfo(self):
        print("\t\t\tSerendipity Booksellers\n")
        print("\t\t\t    Book Information\n\n")
        print("Title: " + self.__title)
        print("ISBN: " + self.__isbn)
        print("Author: " + self.__author)
        print("Publisher: " + self.__publisher)
        print("Date Added: " + self.__date)
        print("Quantity-On-Hand: " + str(self.__qty))
        print("Wholesale Cost: %.2f" % float(self.__wholesale))
        print("Retail Price: %.2f" % float(self.__retail))
        print("\n\n")

    # ***********************************************************************************************************************
    # The to_String function displays various information for different kinds of report choices                             *
    # ***********************************************************************************************************************
    def to_String(self, reportType):
        title = "Title: " + str(self.__title)
        ISBN = "ISBN(#-###-#####-#): " + str(self.__isbn)
        author = "Author: " + str(self.__author)
        publisher = "Publisher: " + str(self.__publisher)
        date = "Date Added to Inventory (MM/DD/YYYY): " + str(self.__date)
        quantity = "Quantity Being Added: " + str(self.__qty)
        wholesale = "Wholesale Cost: " + str(self.__wholesale)
        retail = "Retail Price: " + str(self.__retail)
        if reportType == 1:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n\t{4}\n\t{5}\n\t{6}\n\t{7}\n".format(title,ISBN,author,publisher,date,quantity,wholesale,retail))        
        elif reportType == 2:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title,ISBN,quantity,wholesale))
        elif reportType == 3:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title,ISBN,quantity,retail))
        elif reportType == 4:
            print("\n\t{0}\n\t{1}\n\t{2}\n".format(title,ISBN,quantity))
        elif reportType == 5:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title,ISBN,quantity,wholesale))
        elif reportType == 6:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title,ISBN,quantity,date))
        else:
            print("System Error")
            report()


#####################################################################################
#                                                                                   #
#  PossibleBooksSearcher:looking for any book's title which contain the input String#
#                                                                                   #
#####################################################################################
def booksSearcher(searchTitle, userType):
    i = 0
    found = False
    title = searchTitle.upper()
    matcher = userType.upper()
    length = len(matcher)
    partialTitle = ""
        
    while i < len(title) and found == False:
        partialTitle = title[i:i+length]
        m = SequenceMatcher(None, matcher, partialTitle)
        r = m.ratio()
        if r > .995:
            found = True
        i +=1
    return found

#######################################################################
#                                                                     #
#  Confirming whether the book exactly users want                     #
#                                                                     #
#######################################################################
def correctness(y):
    answer = ""
    correctness = False
        
    answer = y

    if answer == 'n' or answer == 'N':
        correctness = True
        return correctness
    else:
        return correctness

def confirmedBook(index):
    number = 0

    number = index
    print("The book you want is {0}\n".format(listofbooks[number].title))
    listofbooks[number].bookInfo()

###########################################################
#                                                         #
#  The book look up function                              #
#                                                         #
###########################################################
def lookUpBook(enteredTitle):
    found = False
    index = 0
    possibleBooks = []
    searchTitle = enteredTitle
    backToMain = False

    # Search for a matching title.
    ############################
    # loop that runs as long
    #   - found is false
    #   - index is less than the listofbooks size
    #############################

    while index < len(listofbooks) and not backToMain:
        if booksSearcher(listofbooks[index].get_title(),searchTitle) == True:
            possibleBooks.append(index)
        index += 1
            
    if (len(possibleBooks)> 0):
        for i in range(0,len(possibleBooks)):
            print("{0}. \n".format(i+1))
            listofbooks[possibleBooks[i]].bookInfo()
        for r in range(0,len(possibleBooks)):
            print("{0}.\t {1}\n".format(r+1,listofbooks[possibleBooks[r]].get_title()))
        sl = str(input("Can't find the book exactly you want? (Y/N) "))
        if not correctness(sl):
            print("Return to previous menu")
            invMenu()
            backToMain = True
        if len(possibleBooks) == 1:
            p = str(input("Is this book exactly you want? (Y/N) "))
            if p == "y" or p == "Y":
                listofbooks[possibleBooks[0]].bookInfo()
                return possibleBooks[0]
        if not backToMain: 
            n = int(input("Which book do you want ? Please enter the No. "))
            confirmedBook(possibleBooks[n-1])
            return possibleBooks[n-1]
        
    else:
        print("The book you searched for is not in inventory.\n\n")
        return -1



###########################################################
#                                                         #
#  The book's add a new book function                     #
#                                                         #
###########################################################
def addBook():
    # Prompt user for book information
    title = input("Enter Title: ").upper()
    isbn = input("Enter ISBN(#-###-#####-#): ").upper()
    author = input("Enter Author: ").upper()
    publisher = input("Enter Publisher: ").upper()
    date = input("Enter Date Added to Inventory (MM/DD/YYYY): ")
    qty = int(input("Enter Quantity Being Added: "))
    wholesale = float(input("Enter Wholesale Cost: "))
    retail = float(input("Enter Retail Price: "))
        
    # Add the info list to the listofbooks list.
    listofbooks.append(listofbooks(title, isbn, author, publisher, date, qty, wholesale, retail))
    print("\nRecord was successfully entered.\n")	

###########################################################
#                                                         #
#  The book's edit a book function                        #
#                                                         #
###########################################################
def editBook():
    found = False
    index = -1
        
    searchTitle = str(input("Enter the title of the book to edit: "))
    index = lookUpBook(searchTitle)
        
    if index != -1:
        found = True



    # The book was found
    if found:
        choice = 0
        # Ask the user which fields to change, repeat until exit
        while choice != 9:
            print( "\nYou may edit any of the following fields:")
            print( "1. Title")
            print( "2. ISBN")
            print( "3. Author's Name")
            print( "4. Publisher's Name")
            print( "5. Date Book Was Added To Inventory")
            print( "6. Quantity On Hand")
            print( "7. Wholesale Cost")
            print( "8. Retail Price")
            print( "9. Exit\n")
            choice = int(input( "Enter Your Choice: "))

            # Validate the user's input
            while choice < 1 or choice > 9:
                print( "\nPlease enter a number in the range 1 - 9.\n")
                choice = int(input( "Enter Your Choice: "))

            # Set the info variable to the found listofbooks
            info = listofbooks[index]

            # Display the user's choice
            if choice == 1:
                print( "\nCurrent Title: " + info.title)
                info.set_title = input( "Enter new Title:  ").upper()
            elif choice == 2:
                print( "\nCurrent ISBN: " + info.isbn)
                info.set_isbn = input( "Enter new ISBN(#-###-#####-#): ").upper()
            elif choice == 3:
                print( "\nCurrent Author: " + info.author)
                info.set_author(input("Enter new Author: ").upper())
            elif choice == 4:
                print( "\nCurrent Publisher: " + info.publisher)
                info.set_publisher = input( "Enter new Publisher:  ").upper()
            elif choice == 5:
                print( "\nCurrent Date Added: " + info.date)
                info.set_date = input( "Enter new Date(MM/DD/YYYY):  ")
            elif choice == 6:
                print( "\nCurrent Quantity on Hand:  " + str(info.qty))
                info.set_qty = int(input( "Enter new Quantity on Hand:  "))
            elif choice == 7:
                print( "\nCurrent Wholesale Cost:  " + str(info.wholesale))
                info.set_wholesale = float(input( "Enter new Wholesale Cost:  "))
            elif choice == 8:
                print( "\nCurrent Retail Price:  " + str(info.retail))
                info.set_retail = float(input( "Enter new Retail Price:  "))

        # Delete the current book from the list
        # Then add the info list to the listofbooks list
        else:
            del listofbooks[index]
            listofbooks.append(info)
    # The book was not found
    else:
        print( "The book you searched for is not in inventory.\n\n")


###########################################################
#                                                         #
#  The book's delete a book function                      #
#                                                         #
###########################################################
def deleteBook():
    found = False
    index = -1
        
    searchTitle = str(input("Enter the title of the book to delete: "))
    index = lookUpBook(searchTitle)
        
    if index != -1:
        found = True
            
        # Display the book information
        if found:           

            # Confirm book deletion
            confirm = input( "Are you sure you want to delete this book? (Y/N): ")

            # Delete the book
            if confirm == 'Y' or confirm == 'y':
                del listofbooks[index]
                                     
        # The book was not found
        else:
            print( "The book you searched for is not in inventory.\n\n")


# ***********************************************************************
# repListing stub function (reportType = 1)                             *
# ***********************************************************************
def repListing():
    index = 0
    do = True
    trial = ""
    back = ""
    print("\nYou selected Inventory Listing.\n")
    while do == True:
        print("\t\tListing\t\t " + str(datetime.date.today()))
        while index < len(listofbooks):
            listofbooks[index].to_String(1)
            index += 1
        print("\n You left Inventory Listing \n")
        back = str(input(" Return to the previous menu "))
        reports()
        do = False
               
            
        

# **********************************************************************
# repWholesale stub function (reportType = 2)                          *
# **********************************************************************
def repWholesale():    
    index = 0
    do = True
    trial = ""
    back = ""
    total = 0.0
    print("\nYou selected Inventory Wholesale Value.\n")
    while do == True:
        print("\t\tListing\t\t " + str(datetime.date.today()))
        while index < len(listofbooks):
            listofbooks[index].to_String(2)
            total += float(listofbooks[index].qty)* float(listofbooks[index].wholesale)
            index += 1
        print("The total wholesale value of the inventory: " + str(total))
        print("\n You left Inventory Wholesale Value \n")
        back = str(input(" Return to the previous menu "))
        reports()
        do = False
                   

# *************************************************************************
# repRetail stub function (reportType = 3)                                *
# *************************************************************************
def repRetail():
    index = 0
    do = True
    trial = ""
    back = ""
    total = 0.0
    print("\nYou selected Inventory Retail Value.\n")
    while do == True:
        print("\t\tListing\t\t " + str(datetime.date.today()))
        while index < len(listofbooks):
            listofbooks[index].to_String(3)
            total += float(listofbooks[index].retail)*float(listofbooks[index].qty)
            index += 1
        print("The total retail value of the inventory: " + str(total))
        print("\n You left Inventory Retail Value \n")
        back = str(input(" Return to the previous menu "))
        reports()
        do = False
                   

# ***********************************************************************
# repQty stub function (reportType = 4)                                 *
# ***********************************************************************
def repQty():
    index = 0
    do = True
    trial = ""
    back = ""
    list = []
    x = 0
    print("\nYou selected Listing by Quantity.\n")
    while do == True:
        print("\t\tListing\t\t " + str(datetime.date.today()))
        while index < len(listofbooks):
            list.append([listofbooks[index].qty,index])
            index += 1
        list.sort(reverse =True)
        for x in range(len(list)):
            print("{0}. ".format(x+1))
            listofbooks[list[x][1]].to_String(4)
                
        print("\n You left Listing by Quantity \n")
        back = str(input(" Return to the previous menu "))
        reports()
        do = False

# ************************************************************************
# repCost stub function (reportType = 5)                                 *
# ************************************************************************
def repCost():
    index = 0
    do = True
    trial = ""
    back = ""
    list = []
    print("\nYou selected Listing by Cost.\n")
    while do == True:
        print("\t\tListing\t\t " + str(datetime.date.today()))
        while index < len(listofbooks):
            list.append([listofbooks[index].wholesale,index])
            index += 1
        list.sort(reverse =True)
        for x in range(len(list)):
            print("{0}. ".format(x+1))
            listofbooks[list[x][1]].to_String(5)
        print("\n You left Listing Cost \n")
        back = str(input(" Return to the previous menu "))
        reports()
        do = False
                   

# ***********************************************************************
# repAge stub function (reportType = 6)                                 *
# ***********************************************************************
def repAge():
    index = 0
    do = True
    trial = ""
    back = ""
    list = []
    print("\nYou selected Listing by Age.\n")
    while do == True:
        print("\t\tListing\t\t " + str(datetime.date.today()))
        while index < len(listofbooks):
            list.append([listofbooks[index].date,index])
            index += 1
        list = date_sort(list)
        list.reverse()
        for x in range(len(list)):
            print("{0}. ".format(x+1))
            listofbooks[list[x][1]].to_String(6)
        print("\n You left Listing by Age \n")
        back = str(input(" Return to the previous menu "))
        reports()
        do = False
                   

# ********************************************************
# The cashier function displays the Cashier Module       *
# ********************************************************
def cashier():
    SALES_TAX = 0.06	# The sales tax
    # Repeat as long as the user wants to process 
    # another transaction
    again = 'Y'
    while again == 'Y' or again == 'y':
        print( "Serendipity Booksellers\n")
        print( " Cashier Module\n\n")

        # Get the date
        date = input( "Date: ")

        # Get the quantity 
        quantity = int(input( "Quantity of Book: "))


        # Search for a matching title
        found = False
        index = -1
        
        searchTitle = str(input("Enter the title of the book to buy: "))
        index = lookUpBook(searchTitle)
        
        if index != -1:
                found = True

        if not found:
            print("Book not found in the Book Inventory.")
            # Does the user want to process another transaction?
            again = input( "Process another transaction? (Y/N) ")
            continue
          
        # Get the ISBN number
        isbn = listofbooks[index].isbn

        # Get the title
        title = listofbooks[index].title

        # Get the price
        price = int(listofbooks[index].wholesale)

        # Perform the calculations
        # Set the variables to the following values
        #   VARIABLE    |   VALUE
        #   ------------|-----------------------
        #   subtotal    |   quantity * price
        #   tax         |   subtotal * SALES_TAX
        #   total       |   subtotal + tax
        subtotal = quantity * price
        tax = subtotal * SALES_TAX
        total = subtotal + tax

        print( "\n\nSerendipity Book Sellers\n\n")

        # Display the date
        print( "Date: " + date + "\n\n")

        print( "Qty\tISBN\t\tTitle\t\t\t\t\tPrice\t\tTotal")
        print( "_" * 90)
        print( "\n\n")

        # Display the book info
        print( str(quantity) + "\t" + isbn + "\t" + title + "\t\t{0}\t${1}\n".format(price, subtotal)) 

        # Display the calculated totals
        print( "\t\t\t\t\tSubtotal\t\t\t$%.2f" % subtotal)
        print( "\t\t\t\t\tTax\t\t\t\t$%.2f" % tax)
        print( "\t\t\t\t\tTotal\t\t\t\t$%.2f\n" % total)

        print( "\n\nThank You for Shopping at Serendipity!\n")

        # Does the user want to process another transaction?
        again = input( "Process another transaction? (Y/N) ")

# ********************************************************
# The invMenu function displays the Inventory Database   *
# Menu                                                   *
# ********************************************************
def invMenu():
    choice = 0	# To hold the user's choice

    # Display the menu until the user selects item 5
    while choice != 5:
        print( "Serendipity Booksellers\n")
        print( "  Inventory Database\n\n")

        print( "1.Look Up a Book\n")
        print( "2.Add a Book\n")
        print( "3.Edit a Book's Record\n")
        print( "4.Delete a Book\n")
        print( "5.Return to the Main Menu\n\n")

        # Get the choice as input from the user
        choice = int(input( "Enter Your Choice: "))
        
        # Validate the user's input
        while choice < 1 or choice > 5:
            print( "\nPlease enter a number in the range 1 - 5.\n")
            choice = int(input( "Enter Your Choice: "))
                
        # Display the selection
        if choice == 1:
            searchTitle = str(input("Enter the title of the book to search for: "))
            lookUpBook(searchTitle)
        elif choice == 2:
            addBook()
        elif choice == 3:
            editBook()
        elif choice == 4:
            deleteBook()
        else:
            print( "\nYou left the Inventory Menu.\n")
             

# ********************************************************
# The reports function displays the Reports Menu         *
# ********************************************************
def reports():
    choice = 0	# To hold the user's choice
    backToMain = False
    
    # Display the menu until the user selects item 7
    while choice != 7 and not backToMain:
        print( "Serendipity Booksellers\n")
        print( "\tReports\n\n")
        print( "1.Inventory Listing\n")
        print( "2.Inventory Wholesale Value\n")
        print( "3.Inventory Retail Value\n")
        print( "4.Listing by Quantity\n")
        print( "5.Listing by Cost\n")
        print( "6.Listing by Age\n")
        print( "7.Return to the Main Menu\n\n")

        # Get the choice as input from the user
        choice = int(input( "Enter Your Choice: "))
        
        # Validate the user's input
        while choice < 1 or choice > 7:
            print( "\nPlease enter a number in the range 1 - 7.\n")
            choice = int(input( "Enter Your Choice: "))                

        # Display the selection
        if choice == 1:
            repListing()
            backToMain = True
        elif choice == 2:
            repWholesale()
            backToMain = True
        elif choice == 3:
            repRetail()
            backToMain = True
        elif choice == 4:
            repQty()
            backToMain = True
        elif choice == 5:
            repCost()
            backToMain = True
        elif choice == 6:
            repAge()
            backToMain = True
        else:
            print( "\nYou left the Reports Menu.\n")




# ********************************************************
# The date sorting function                              *   #Resource from http://www.cnblogs.com/lkprof/p/3179850.html
# ********************************************************
def changeDateFormat(date):
    d = date
    year = d[-4:]
    f = year + "/"+ d[:-5]
    return f


def date_sort(x):
    ls=list(x)

    for f in range(len(ls)):
        ls[f][0] = changeDateFormat(ls[f][0])

    for j in range(len(ls)-1):
        for i in range(len(ls)-j-1):
            lower=ls[i][0].split('/')
            upper=ls[i+1][0].split('/')       
            for s in range(3):
                if int(lower[s])>int(upper[s]):                
                    ls[i],ls[i+1]=ls[i+1],ls[i]
                    break
                elif int(lower[s])<int(upper[s]):
                    break
    ar=list(ls)
    return ar



# *****************************************************************************************************
# The Input filter fuction that read from the File and Add the listofbooks objects to the listofbooks list. *
# *****************************************************************************************************
def inputFilter(file):
    items = []
    filebaseline = open(file, "r")
    while True:
        items = []
        book = filebaseline.readline()
        if len(book) == 0:
            break
        for i in range(8):
            index = book.find('#')            
            item = book[:index]
            book = book[index+1:]
            items.append(item)
        listofbooks.append(listofbooks(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7]))
    filebaseline.close()



# *************************************************************************************************************************
# The Output filter that write the curent listofbooks list of listofbooks objects to the file, when the user exits the program *
# *************************************************************************************************************************
def outputFilter():
    filebaseline = open("filebaseline.txt", "w")
    for i in range(len(listofbooks)):
        book = "{0}#{1}#{2}#{3}#{4}#{5}#{6}#{7}\n".format(listofbooks[i].title,listofbooks[i].isbn,listofbooks[i].author,listofbooks[i].publisher,listofbooks[i].date,listofbooks[i].qty,listofbooks[i].wholesale,listofbooks[i].retail)
        filebaseline.write(book)
    filebaseline.close()

                          
#######################################
#   Main Program
#######################################
choice = 0	# To hold the user's menu choice

# Create an Inventory File and include the current Book Information that we have in the code.  Also want you to add 2 new books to that list.
try:
    filebaseline = open("filebaseline.txt", "w")
except IOError as err:
    print("Could not write file: ", err)
    sys.exit()
try:  
    filebaseline.write("Introducing Python#978-1-4493-5936-2#Bill Lubanovic#O'Reilly Media, Inc.#11/24/2014#25#39.95#50.00#\n")
    filebaseline.write("Pro Python#978-1-4842-0335-4#J. Burton Browning, Marty Alchin#Apress#6/24/2014#45#35.50#49.99#\n")
    filebaseline.write("Information Technology Project Management#978-1-2854-5234-0#Kathy Schwalbe#Cengage#11/9/2015#35#100.25#179.00#\n")
    filebaseline.write("Starting Out with C++: From Control Structures through Objects#978-0-1337-6939-5#Tony Gaddis#Cengage#11/8/2015#15#105.00#175.00#\n")
    filebaseline.write("Learn More/104#11-1-2243-0000-5#Putun, Ahmet#PSUAhmet#1/21/2007#70#99#300#\n")
    filebaseline.write("Knowledge of Universe/140#21-1-4349-9998-7#Putun, Ahmet#PSUAhmet#2/42/2020#6#100#170#\n")
    filebaseline.close()
except IOError as optErr:
    print("Unsupported Operation: ", optErr)
    sys.exit()

try:
    inputFilter("filebaseline.txt")
except IOError as err1:
    print("Could not read file: ", err1)
    sys.exit()




# Display the menu until the user selects item 4
while choice != 4:
    print( "Serendipity Booksellers\n")
    print( "\tMain Menu\n\n")

    print( "1.Cashier Module\n")
    print( "2.Inventory Database Module\n")
    print( "3.Report Module\n")
    print( "4.Exit\n\n")

    # Get the menu choice as input from the user
    choice = int(input("Enter Your Choice: "))
    
    # Validate the user's input
    while choice < 1 or choice > 4:
        print( "\nPlease enter a number in the range 1 - 4.\n")
        choice = int(input( "Enter Your Choice: "))
            
    # Display the selection
    if choice == 1:
        cashier()
    elif choice == 2:
        invMenu()
    elif choice == 3:
        reports()
    else:
        try:
            outputFilter()
        except IOError as err2:
            print("Could not write file: ",err2)
            sys.exit()
        finally:
            '''(This is for testing
            f = open("listofbooksProject3.txt")
            content = f.read()
            print(content)
            '''
            print("Leaving the Book Inventory Program")
