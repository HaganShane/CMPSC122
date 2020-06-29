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
#  author:    The author’s name                           #
#  publisher: The publisher’s name                        #
#  date:      The date the book was added to inventory    #
#  qty:       The quantity on hand of the book            #
#  wholesale: The wholesale cost of the book              #
#  retail:    The retail price of the book                #
###########################################################

############################
# Create a list named bookData.
#   Initialize the list to an empty list
#############################
bookData = []

###########################################################
#                                                         #
#             Create BookData Class                       #
#                                                         #
#                                                         #
###########################################################
class BookData():
    def __init__(self, title, isbn, author, publisher, date, qty, wholesale, retail):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.date = date
        self.qty = qty
        self.wholesale = wholesale
        self.retail = retail
    def to_string(self):
        return "Title: {0}, ISBN: {1}, Author: {2}, Publisher: {3}, Date Added: {4}, Quantity On Hand: {5}, Wholesale Cost: {6}, Retail Cost: {7}".format(self.title, self.isbn, self.author, self.publisher, self.date, self.qty, self.wholesale, self.retail)
        


###########################################################
#                                                         #
#  The bookInfo function displays the Book Information    #
#  Screen                                                 #
#                                                         #
###########################################################
def bookInfo(book):
    print("\t\t\tSerendipity Booksellers\n")
    print("\t\t\t    Book Information\n\n")
    print("Title: " + book.title)
    print("ISBN: " + book.isbn)
    print("Author: " + book.author)
    print("Publisher: " + book.publisher)
    print("Date Added: " + book.date)
    print("Quantity-On-Hand: " + str(book.qty))
    print("Wholesale Cost: %.2f" % float(book.wholesale))
    print("Retail Price: %.2f" % float(book.retail))
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
    for book in bookData:
        if book.title.upper().find(searchTitle.upper()) > 0:
            NewList.append(str(index + 1) + "." + book.title)
        index += 1

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
    info = []
    # Prompt user for book information
    info.append(str.upper(input("Enter Title: ")))
    info.append(str.upper(input("Enter ISBN(#-###-#####-#): ")))
    info.append(str.upper(input("Enter Author: ")))
    info.append(str.upper(input("Enter Publisher: ")))
    info.append(input("Enter Date Added to Inventory (MM/DD/YYYY): "))
    info.append(int(input("Enter Quantity Being Added: ")))
    info.append(float(input("Enter Wholesale Cost: ")))
    info.append(float(input("Enter Retail Price: ")))
    
    # Add the info list to the bookData list.
    bookData.append(info)
    print("\nRecord was successfully entered.\n")	

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
    for book in bookData:
        if book.title.upper().find(searchTitle.upper()) > 0:
            NewList.append(str(index + 1) + "." + book.title)
        index += 1

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

                # Set the info variable to the found bookData
                info = BookData.to_string(book)

                # Display the user's choice
                if choice == 1:
                    print( "\nCurrent Title: " + book.title)
                    info[0] = str.upper(input( "Enter new Title:  "))
                elif choice == 2:
                    print( "\nCurrent ISBN: " + book.isbn)
                    info[1] = str.upper(input( "Enter new ISBN(#-###-#####-#): "))
                elif choice == 3:
                    print( "\nCurrent Author: " + book.author)
                    info[2] = str.upper(input("Enter new Author: "))
                elif choice == 4:
                    print( "\nCurrent Publisher: " + book.publisher)
                    info[3] = str.upper(input( "Enter new Publisher:  "))
                elif choice == 5:
                    print( "\nCurrent Date Added: " + book.date)
                    info[4] = input( "Enter new Date(MM/DD/YYYY):  ")
                elif choice == 6:
                    print( "\nCurrent Quantity on Hand:  " + str(book.qty))
                    info[5] = int(input( "Enter new Quantity on Hand:  "))
                elif choice == 7:
                    print( "\nCurrent Wholesale Cost:  " + str(book.wholesale))
                    info[6] = float(input( "Enter new Wholesale Cost:  "))
                elif choice == 8:
                    print( "\nCurrent Retail Price:  " + str(book.retail))
                    info[7] = float(input( "Enter new Retail Price:  "))

                # Delete the current book from the list
                # Then add the info list to the bookData list
                else:
                    del bookData[index]
                    bookData.append(info)
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
    for book in bookData:
        if book.title.upper().find(searchTitle.upper()) > 0:
            NewList.append(str(index + 1) + "." + book.title)
        index += 1

    if len(NewList) > 0:
        titleNumbers = []
        print("Select a book from the list: ")
        for title in NewList:
            titleNumbers.append(int(title[0]))
            print(title)
        userchoice = int(input("Book Number: "))

        if userchoice in titleNumbers:
            book = bookData[userchoice -1]
            del book
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
    for book in bookData:
        print(b, "." ,book.title,"/", book.isbn,"/", book.author,"/", book.publisher,"/", book.date,"/", book.qty,"/", book.wholesale,"/", book.retail,"\n")
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
    for book in bookData:
        print(b, "." ,book.title,"/", book.isbn,"/",book.qty,"/", book.wholesale,"\n")
        TotalWholesale += book.qty * book.wholesale
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
    for book in bookData:
        print(b, "." ,book.title,"/", book.isbn,"/",book.qty,"/", book.retail,"\n")
        TotalRetail += book.qty * book.retail
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
    QuantityList = sorted(bookData, key = lambda x: x.qty, reverse = True)
    a = 0
    b = 1
    print("Sorted List size: " + str(len(QuantityList)))
    for book in QuantityList:
        print(b, "." ,book.title,"/",book.isbn,"/",book.qty,"\n")
        a += 1
        b += 1

# ********************************************************
# repCost stub function                                  *
# ********************************************************
def repCost():
    print( "\nYou selected Listing By Cost.\n")
    print("\nToday's Cost Report,", datetime.date.today(),"\n")
    print("(List formatted as Title/ISBN Number/Quantity On Hand/Wholesale Price, in decending order according to wholesale price)\n")
    CostList = []
    CostList = sorted(bookData, key = lambda x: x.wholesale, reverse= True)
    a = 0
    b = 1
    for book in CostList:
        print(b, "." ,book.title,"/",book.isbn,"/",book.qty,"/",book.wholesale,"\n")
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
    AgeList = sorted(bookData, key=lambda k: (datetime.datetime.strptime(k.date,'%m/%d/%Y').date()))
    a = 0
    b = 1
    for book in AgeList:
        print(b, "." ,book.title,"/",book.isbn,"/",book.qty,"/",book.date,"\n")
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
        quantity = int(input( "Quantity of Book: "))

        searchTitle = input( "Enter the title of the book to buy: ")
        found = False
        index = 0

        # Search for a matching title
        for book in bookData:
            if book.title == searchTitle:
                found = True
            else:
                index += 1

        if not found:
            print("Book not found in the Book Inventory.")
            # Does the user want to process another transaction?
            again = input( "Process another transaction? (Y/N) ")
            continue
      
        # Get the ISBN number
        isbn = book.isbn

        # Get the title
        title = book.title

        # Get the price
        price = int(book.retail)

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
            choice = int(print( "Enter Your Choice: "))
                
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
#Pre set some books into the Book Inventory
'''bookData.append(BookData("Introducing Python", "978-1-4493-5936-2", "Bill Lubanovic", "O'Reilly Media, Inc.", "11/24/2014", 25, 39.95, 50.00))
bookData.append(BookData("Pro Python", "978-1-4842-0335-4", "J. Burton Browning, Marty Alchin", "Apress", "6/24/2014", 25, 35.50, 49.99))
bookData.append(BookData("Information Technology Project Management", "978-1-2854-5234-0", "Kathy Schwalbe", "Cengage", "11/6/2015", 25, 100.25, 179.00))
bookData.append(BookData("Starting Out with C++: From Control Structures through Objects", "978-0-1337-6939-5", "Tony Gaddis", "Cengage", "11/6/2015", 15, 105.00, 175.00))'''

### Inventory File ###
def GetBooks():
    try:
        f = open("Inventory.txt", "r")
        for line in f:
            print(line)
            LineSplit = line.split(",")
            bookData.append(BookData(LineSplit[0], LineSplit[1], LineSplit[2], LineSplit[3], LineSplit[4], LineSplit[5], LineSplit[6], LineSplit[7]))
            print(bookData)
    except:
        print("The inventory was unable to be obtained")

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
