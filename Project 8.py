####################################
#                                  #
# CMPSC 122 Project Baseline       #
#                                  #
####################################
import datetime
import operator
import time
import re
###########################################################
# bookData will consist of the following information      #
#  title:     The book title                              #
#  isbn:      The ISBN number of a book                   #
#  author:    The author's name                           #
#  publisher: The publisher's name                        #
#  date:      The date the book was added to inventory    #
#  qty:       The quantity on hand of the book            #
#  wholesale: The wholesale cost of the book              #
#  retail:    The retail price of the book                #
###########################################################



###########################################################
#                                                         #
#             Create BookData Class                       #
#                                                         #
#                                                         #
###########################################################
class BookData():
    def __init__(self, title, isbn, author, publisher):
        self.__title = title
        self.__isbn = isbn
        self.__author = author
        self.__publisher = publisher

### Get and Set Functions ###
    def SetTitle(self, title):
        self.__title = title
    def GetTitle(self):
        return self.__title
    def SetIsbn(self, isbn):
        self.__isbn = isbn
    def GetIsbn(self):
        return self.__isbn
    def SetAuthor(self, author):
        self.__author = author
    def GetAuthor(self):
        return self.__author
    def SetPublisher(self, publisher):
        self.__publisher = publisher
    def GetPublisher(self):
        return self.__publisher

    

    def to_string(self):
        return "Title: {0}, ISBN: {1}, Author: {2}, Publisher: {3}, Date Added: {4}, Quantity On Hand: {5}, Wholesale Cost: {6}, Retail Cost: {7}".format(self.GetTitle(), self.GetIsbn(), self.GetAuthor(), self.GetPublisher(), self.GetDate(), self.GetQty(), self.GetWholesale(), self.GetRetail())

###########################################################
#                                                         #
#             Create InventoryBook Class                  #
#                                                         #
#                                                         #
###########################################################
class InventoryBook(BookData):
    def __init__(self, title, isbn, author, publisher, date, qty, wholesale, retail):
        BookData.__init__(self, title, isbn, author, publisher)
        self.__date = date
        self.__qty = qty
        self.__wholesale = wholesale
        self.__retail = retail

    # Get and Set
    def SetDate(self, date):
        self.__date = date
    def GetDate(self):
        return self.__date
    def SetQty(self, qty):
        self.__qty = qty
    def GetQty(self):
        return self.__qty
    def SetWholesale(self, wholesale):
        self.__wholesale = wholesale
    def GetWholesale(self):
        return self.__wholesale
    def SetRetail(self, retail):
        self.__retail = retail
    def GetRetail(self):
        return self.__retail 

    def to_string(self):
        return "Title: {0}, ISBN: {1}, Author: {2}, Publisher: {3}, Date Added: {4}, Quantity On Hand: {5}, Wholesale Cost: {6}, Retail Cost: {7}".format(self.GetTitle(), self.GetIsbn(), self.GetAuthor(), self.GetPublisher(), self.GetDate(), self.GetQty(), self.GetWholesale(), self.GetRetail())


###########################################################
#                                                         #
#             Create SoldBook Class                       #
#                                                         #
#                                                         #
###########################################################
class SoldBook(InventoryBook):
    taxRate = .06
    total = 0 
    def __init__(self, qtySold, title, isbn, author, publisher, date, qty, wholesale, retail):
        InventoryBook.__init__(self, title, isbn, author, publisher, date, qty, wholesale, retail)
        self.__qtySold = qtySold
        self.__tax = SoldBook.taxRate * retail * qtySold
        self.__subtotal = (retail * qtySold)

    # Set Functions
    def GetTax(self):
        return self.__tax
    def GetSubTotal(self):
        return self.__subtotal




###########################################################
#                                                         #
#             Create Linked List Class                    #
#                                                         #
#                                                         #
###########################################################
class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

def InsertNode(node, val):
    NewNode = Node(val)
    if node.cargo is None:
        node.cargo = val
        node.next = None
    else:
        while node.next is not None:
            node = node.next
        node.next = NewNode


def DeleteNode(node, val):
    while node is not None:
        if val.GetIsbn() == node.cargo.GetIsbn(): 
            prev.next = node.next
            node.next = None
            return





###########################################################
#                                                         #
#  The bookInfo function displays the Book Information    #
#  Screen                                                 #
#                                                         #
###########################################################
def bookInfo(book):
    print("\t\t\tSerendipity Booksellers\n")
    print("\t\t\t    Book Information\n\n")
    print("Title: " + book.GetTitle())
    print("ISBN: " + book.GetIsbn())
    print("Author: " + book.GetAuthor())
    print("Publisher: " + book.GetPublisher())
    print("Date Added: " + book.GetDate())
    print("Quantity-On-Hand: " + str(book.GetQty()))
    print("Wholesale Cost: %.2f" % float(book.GetWholesale()))
    print("Retail Price: %.2f" % float(book.GetRetail()))
    print("\n\n")

###########################################################
#                                                         #
#  The book look up function                              #
#                                                         #
###########################################################
def lookUpBook():
    index = 0
    
    searchTitle = input("Enter the title of the book to search for: ")
    NewList = []
    

    # Search for a matching title using partial titles
    node = bookData
    while node is not None:
        book = node.cargo
        if book.GetTitle().upper().find(searchTitle.upper()) >= 0:
            NewList.append(str(index + 1) + "." + book.GetTitle())
        index += 1
        node = node.next

    if len(NewList) > 0:
        titleNumbers = []
        print("Select a book from the list: ")
        for title in NewList:
            titleNumbers.append(int(title[0]))
            print(title)
        choice = int(input("Book Number: "))

        if choice in titleNumbers:
            bookInfo(bookData[choice - 1])
        else:
            print("Invalid Selection.")
    else:
        print("The book you searched for is not in the inventory.")
        

###########################################################
#                                                         #
#  The book's add a new book function                     #
#                                                         #
###########################################################
def addBook():
    # Prompt user for book information
    title = (str.upper(input("Enter Title: ")))
    isbn = (str.upper(input("Enter ISBN(#-###-#####-#): ")))
    author = (str.upper(input("Enter Author: ")))
    publisher = (str.upper(input("Enter Publisher: ")))
    date = (input("Enter Date Added to Inventory (MM/DD/YYYY): "))
    try:   
        qty = (int(input("Enter Quantity Being Added: ")))
    except:
        print("Invalid: You must enter a valid quantity")
    try:
        wholesale = (float(input("Enter Wholesale Cost: ")))
    except:
        print("Invalid: You must enter a valid price")
    try:
        retail = (float(input("Enter Retail Price: ")))
    except:
        print("Invalid: You must enter a valid price")
    
    # Add the info list to the bookData list.
    try:
        InsertNode(bookData, InventoryBook(title, isbn, author, publisher, date, qty, wholesale, retail))
        print("\nRecord was successfully entered.\n")
    except:
        print("Error: Due to invalid quantity or price, the book was not entered successfully")

###########################################################
#                                                         #
#  The book's edit a book function                        #
#                                                         #
###########################################################
def editBook():	
    index = 0	        # The book title array index

    # Get the book title to search for from the user
    searchTitle = input("Enter the title of the book to edit: ")


    NewList = []
    node = bookData
    while node is not None:
        book = node.cargo
        if book.GetTitle().upper().find(searchTitle.upper()) >= 0:
            NewList.append(str(index + 1) + "." + book.GetTitle())
        index += 1
        node = node.next

    if len(NewList) > 0:
        titleNumbers = []
        print("Select a book from the list: ")
        for title in NewList:
            titleNumbers.append(int(title[0]))
            print(title)
        userchoice = int(input("Book Number: "))

        if userchoice in titleNumbers:
            book = bookData[userchoice -1]
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


                # Display the user's choice
                if choice == 1:
                    print( "\nCurrent Title: " + str(book.GetTitle()))
                    book.SetTitle(str.upper(input( "Enter new Title:  ")))
                elif choice == 2:
                    print( "\nCurrent ISBN: " + book.GetIsbn())
                    book.SetIsbn(str.upper(input( "Enter new ISBN(#-###-#####-#): ")))
                elif choice == 3:
                    print( "\nCurrent Author: " + book.GetAuthor())
                    book.SetAuthor(str.upper(input("Enter new Author: ")))
                elif choice == 4:
                    print( "\nCurrent Publisher: " + book.GetPublisher())
                    book.SetPublisher(str.upper(input( "Enter new Publisher:  ")))
                elif choice == 5:
                    print( "\nCurrent Date Added: " + book.GetDate())
                    book.SetDate(input( "Enter new Date(MM/DD/YYYY):  "))
                elif choice == 6:
                    print( "\nCurrent Quantity on Hand:  " + str(book.GetQty()))
                    try:
                        book.SetQty(int(input( "Enter new Quantity on Hand:  ")))
                    except:
                        print("\nError: You must enter a valid quantity.\n")
                elif choice == 7:
                    print( "\nCurrent Wholesale Cost:  " + str(book.GetWholesale()))
                    try:
                        book.SetWholesale(float(input( "Enter new Wholesale Cost:  ")))
                    except:
                        print("\nError: You must enter a valid price.\n") 
                elif choice == 8:
                    print( "\nCurrent Retail Price:  " + str(book.GetRetail()))
                    try:  
                        book.SetRetail(float(input( "Enter new Retail Price:  ")))
                    except:
                        print("\nError: You must enter a valid price.\n")
        else:
            print("Invalid Selection.")
    

            
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
    index = 0

    # Get the book title as input from the user
    searchTitle = input( "Enter the title of the book to delete: ")

    NewList = []
    BookList = []
    node = bookData
    while node is not None:
        book = node.cargo
        if book.GetTitle().upper().find(searchTitle.upper()) >= 0:
            NewList.append(str(index + 1) + "." + book.GetTitle())
        index += 1
        node = node.next

    if len(NewList) > 0:
        titleNumbers = []
        print("Select a book from the list: ")
        for title in NewList:
            titleNumbers.append(int(title[0]))
            print(title)
        userchoice = int(input("Book Number: "))
        NodeList = []
        NodeList.append(InventoryBook(node.cargo))

        if userchoice in titleNumbers:
            DeleteNode(bookData, NodeList)
            print("The book has been deleted, thank you\n\n")

    
                                 
        # The book was not found
        else:
            print( "The book you searched for is not in inventory.\n\n")


# ********************************************************
# repListing stub function                               *
# ********************************************************
def repListing():
    print( "\nYou selected Inventory Listing.\n")
    a = 0
    b = 1
    print("\nToday's Listing Report,", datetime.date.today(),"\n")
    print("(List formatted as Title/ISBN Number/Author/Publisher/Date Added/Quantity On Hand/Wholesale Price/Retail Price)\n")
    ReportList = []
    node = bookData
    while node is not None:
        ReportList.append(node.cargo)
        node = node.next
    for book in ReportList:
        print(b, "." ,book.GetTitle(),"/", book.GetIsbn(),"/", book.GetAuthor(),"/", book.GetPublisher(),"/", book.GetDate(),"/", book.GetQty(),"/", book.GetWholesale(),"/", book.GetRetail(),"\n")
        a += 1
        b += 1
    
# ********************************************************
# repWholesale stub function                             *
# ********************************************************
def repWholesale():
    print( "\nYou selected Inventory Wholesale Value.\n")
    print("\nToday's Wholesale Report,", datetime.date.today(),"\n")
    print("(List formatted as Title/ISBN Number/Quantity On Hand/Wholesale Price)\n")
    a = 0
    b = 1
    TotalWholesale = 0
    ReportList = []
    node = bookData
    while node is not None:
        ReportList.append(node.cargo)
        node = node.next
    for book in ReportList:
        print(b, "." ,book.GetTitle(),"/", book.GetIsbn(),"/",book.GetQty(),"/", book.GetWholesale(),"\n")
        TotalWholesale += float(book.GetQty()) * float(book.GetWholesale())
        a += 1
        b += 1
    print("The total wholesale value for all books in the inventory is","$",TotalWholesale,"\n")
        

# ********************************************************
# repRetail stub function                                *
# ********************************************************
def repRetail():
    print( "\nYou selected Inventory Retail Value.\n")
    print("\nToday's Retail Report,", datetime.date.today(),"\n")
    print("(List formatted as Title/ISBN Number/Quantity On Hand/Retail Price)\n")
    a = 0
    b = 1
    TotalRetail = 0
    ReportList = []
    node = bookData
    while node is not None:
        ReportList.append(node.cargo)
        node = node.next 
    for book in ReportList:
        print(b, "." ,book.GetTitle(),"/", book.GetIsbn(),"/",book.GetQty(),"/", book.GetRetail(),"\n")
        TotalRetail += float(book.GetQty()) * float(book.GetRetail())
        a += 1
        b += 1
    print("The total retail value for all books in the inventory is","$",TotalRetail,"\n")

# ********************************************************
    # repQty stub function                                   *
# ********************************************************
def repQty():
    print( "\nYou selected Listing By Quantity.\n")
    print("\nToday's Quantity Report,", datetime.date.today(),"\n")
    print("(List formatted as Title/ISBN Number/Quantity On Hand, in decending order according to quantity)\n")
    QuantityList = []
    ReportList = []
    node = bookData
    while node is not None:
        ReportList.append(node.cargo)
        node = node.next
    QuantityList = sorted(ReportList, key = lambda x: x.GetQty(), reverse = True)
    a = 0
    b = 1
    print("Sorted List size: " + str(len(QuantityList)))
    for book in QuantityList:
        print(b, "." ,book.GetTitle(),"/",book.GetIsbn(),"/",book.GetQty(),"\n")
        a += 1
        b += 1

# ********************************************************
# repCost stub function                                  *
# ********************************************************
def repCost():
    print( "\nYou selected Listing By Cost.\n")
    print("\nToday's Cost Report,", datetime.date.today(),"\n")
    print("(List formatted as Title/ISBN Number/Quantity On Hand/Wholesale Price, in decending order according to wholesale price)\n")
    ReportList = []
    node = bookData
    while node is not None:
        ReportList.append(node.cargo)
        node = node.next
    CostList = []
    CostList = sorted(ReportList, key = lambda x: x.GetWholesale(), reverse= True)
    a = 0
    b = 1
    for book in CostList:
        print(b, "." ,book.GetTitle(),"/",book.GetIsbn(),"/",book.GetQty(),"/",book.GetWholesale(),"\n")
        a += 1
        b += 1
    
# ********************************************************
# repAge stub function                                   *
# ********************************************************
def repAge():
    print( "\nYou selected Listing By Age.\n")
    print("\nToday's Age Report,", datetime.date.today(),"\n")
    print("(List formatted as Title/ISBN Number/Quantity On Hand/Date Added, in decending order according to date added)\n")
    AgeList = []
    ReportList = []
    node = bookData
    while node is not None:
        ReportList.append(node.cargo)
        node = node.next
    AgeList = sorted(ReportList, key=lambda k: (datetime.datetime.strptime(k.GetDate(),'%m/%d/%Y').date()))
    a = 0
    b = 1
    for book in AgeList:
        print(b, "." ,book.GetTitle(),"/",book.GetIsbn(),"/",book.GetQty(),"/",book.GetDate(),"\n")
        a += 1
        b += 1

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
        try:
            quantity = int(input( "Quantity of Book: "))
        except:
            print("Error: You must enter a valid quantity")

        searchTitle = input( "Enter the title of the book to buy: ")
        found = False
        index = 0
        
        
        # Search for a matching title
        for book in bookData:
            if book.GetTitle() == searchTitle:
                found = True
                break
            else:
                index += 1

        if not found:
            print("Book not found in the Book Inventory.")
            # Does the user want to process another transaction?
            again = input( "Process another transaction? (Y/N) ")
            continue
      
        # Get the ISBN number
        isbn = book.GetIsbn()

        # Get the title
        title = book.GetTitle()

        # Get the price
        price = float(book.GetRetail())

        # Perform the calculations
        # Set the variables to the following values
        #   VARIABLE    |   VALUE
        #   ------------|-----------------------
        #   subtotal    |   quantity * price
        #   tax         |   subtotal * SALES_TAX
        #   total       |   subtotal + tax

        ### SoldBook Class ###
        SBook = SoldBook(quantity, book.GetTitle(), book.GetIsbn(), book.GetAuthor(), book.GetPublisher(), book.GetDate(), book.GetQty(), book.GetWholesale(), book.GetRetail())
        subtotal = SBook.GetSubTotal()
        tax = SBook.GetTax()
        total = subtotal + tax

        BookList = []
        BookList.append(SBook)

        # Does the user want to process another transaction?
        again = input( "Process another transaction? (Y/N) ")


        if again == "n" or again == "N":
            print( "\n\nSerendipity Book Sellers\n\n")

            # Display the date
            print( "Date: " + date + "\n\n")

            print( "Qty\tISBN\t\tTitle\t\t\t\t\tPrice\t\tTotal")
            print( "_" * 90)
            print( "\n\n")

            

            for book in BookList:
            # Display the book info
                print( str(SBook.GetQty()) + "\t" + SBook.GetIsbn() + "\t" + SBook.GetTitle() + "\t\t{0}\t${1}\n".format(price, subtotal)) 

                # Display the calculated totals
                print( "\t\t\t\t\tSubtotal\t\t\t$%.2f" % subtotal)
                print( "\t\t\t\t\tTax\t\t\t\t$%.2f" % tax)
                print( "\t\t\t\t\tTotal\t\t\t\t$%.2f\n" % total)

                print( "\n\nThank You for Shopping at Serendipity!\n")

        

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
            choice = int(input("Enter Your Choice: "))
                
        # Display the selection
        if choice == 1:
            lookUpBook()
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
    UserInput = 0
    # Display the menu until the user selects item 7
    while choice != 7:
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
            UserInput = input("Would you like to be redirected back to the Reports Menu? ") # Will always direct user back to menu, no matter the input
        elif choice == 2:
            repWholesale()
            UserInput = input("Would you like to be redirected back to the Reports Menu? ") # Will always direct user back to menu, no matter the input
        elif choice == 3:
            repRetail()
            UserInput = input("Would you like to be redirected back to the Reports Menu? ") # Will always direct user back to menu, no matter the input
        elif choice == 4:
            repQty()
            UserInput = input("Would you like to be redirected back to the Reports Menu? ") # Will always direct user back to menu, no matter the input
        elif choice == 5:
            repCost()
            UserInput = input("Would you like to be redirected back to the Reports Menu? ") # Will always direct user back to menu, no matter the input
        elif choice == 6:
            repAge()
            UserInput = input("Would you like to be redirected back to the Reports Menu? ") # Will always direct user back to menu, no matter the input
            
        else:
            print( "\nYou left the Reports Menu.\n")


#######################################
#   Main Program
#######################################
choice = 0	# To hold the user's menu choice

bookData = Node()

### Inventory File ###
def GetBooks():
        f = open("Inventory.txt", "r")
        for line in f:
            LineSplit = line.split(",")
            InsertNode(bookData, InventoryBook(LineSplit[0], str(LineSplit[1]), LineSplit[2], LineSplit[3], LineSplit[4], float(LineSplit[5]), float(LineSplit[6]), float(LineSplit[7])))
            
       #except:
           # print("The inventory was unable to be obtained")

GetBooks()




def WriteBooks():
    try:
        f = open("Inventory.txt", "w")
        f.write(bookData)
    except:
        print("Unable to add to inventory")


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
        WriteBooks()
        print("Leaving the Book Inventory Program")
