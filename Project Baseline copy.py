####################################
#                                  #
# CMPSC 122 Project Baseline       #
#                                  #
####################################
import datetime
import operator
import time
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
#  The bookInfo function displays the Book Information    #
#  Screen                                                 #
#                                                         #
###########################################################
def bookInfo(bookData):
    print("\t\t\tSerendipity Booksellers\n")
    print("\t\t\t    Book Information\n\n")
    print("Title: " + bookData[0])
    print("ISBN: " + bookData[1])
    print("Author: " + bookData[2])
    print("Publisher: " + bookData[3])
    print("Date Added: " + bookData[4])
    print("Quantity-On-Hand: " + str(bookData[5]))
    print("Wholesale Cost: %.2f" % float(bookData[6]))
    print("Retail Price: %.2f" % float(bookData[7]))
    print("\n\n")

###########################################################
#                                                         #
#  The book look up function                              #
#                                                         #
###########################################################
def lookUpBook():
    found = False
    index = 0
    
    searchTitle = input("Enter the title of the book to search for: ")

    # Search for a matching title.
    ############################
    # loop that runs as long
    #   - found is false
    #   - index is less than the bookData size
    #############################
    while not found and index < len(bookData):
        if bookData[index][0] == searchTitle:
            found = True
        else:
            index += 1

    if found:
        ############################
        # Call the bookInfo function
        #   -Pass in the found list from bookData
        #############################
        bookInfo(bookData[index])
    else:
        print("The book you searched for is not in inventory.\n\n")

###########################################################
#                                                         #
#  The book's add a new book function                     #
#                                                         #
###########################################################
def addBook():
    info = []
    # Prompt user for book information
    info.append(input("Enter Title: "))
    info.append(input("Enter ISBN(#-###-#####-#): "))
    info.append(input("Enter Author: "))
    info.append(input("Enter Publisher: "))
    info.append(input("Enter Date Added to Inventory (MM-DD-YYYY): "))
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
    found = False	# The book title found flag
    index = 0	        # The book title array index

    # Get the book title to search for from the user
    searchTitle = input("Enter the title of the book to edit: ")

    # Search for a matching book title
    while not found and index < len(bookData):
        if bookData[index][0] == searchTitle:
            found = True
        else:
            index += 1

    # The book was found
    if found:
        # Display the results
        bookInfo(bookData[index])

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
            info = bookData[index]

            # Display the user's choice
            if choice == 1:
                print( "\nCurrent Title: " + info[0])
                info[0] = input( "Enter new Title:  ")
            elif choice == 2:
                print( "\nCurrent ISBN: " + info[1])
                info[1] = input( "Enter new ISBN(#-###-#####-#): ")
            elif choice == 3:
                print( "\nCurrent Author: " + info[2])
                info[2] = input("Enter new Author: ")
            elif choice == 4:
                print( "\nCurrent Publisher: " + info[3])
                info[3] = input( "Enter new Publisher:  ")
            elif choice == 5:
                print( "\nCurrent Date Added: " + info[4])
                info[4] = input( "Enter new Date(MM-DD-YYYY):  ")
            elif choice == 6:
                print( "\nCurrent Quantity on Hand:  " + str(info[5]))
                info[5] = int(input( "Enter new Quantity on Hand:  "))
            elif choice == 7:
                print( "\nCurrent Wholesale Cost:  " + str(info[6]))
                info[6] = float(input( "Enter new Wholesale Cost:  "))
            elif choice == 8:
                print( "\nCurrent Retail Price:  " + str(info[7]))
                info[7] = float(input( "Enter new Retail Price:  "))

        # Delete the current book from the list
        # Then add the info list to the bookData list
        else:
            del bookData[index]
            bookData.append(info)
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

    # Search for a matching title
    while not found and index < len(bookData):
        if bookData[index][0] == searchTitle:
            found = True
        else:
            index += 1

        # Display the book information
        if found:
            # Call the bookInfo function
            bookInfo(bookData[index])            

            # Confirm book deletion
            confirm = input( "Are you sure you want to delete this book? (Y/N): ")

            # Delete the book
            if confirm == 'Y' or confirm == 'y':
                del bookData[index]
                                 
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
    while a < int(len(bookData)):
        print(b, "." ,bookData[a][0],"/", bookData[a][1],"/", bookData[a][2],"/", bookData[a][3],"/", bookData[a][4],"/", bookData[a][5],"/", bookData[a][6],"/", bookData[a][7],"\n")
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
    while a < int(len(bookData)):
        print(b, "." ,bookData[a][0],"/", bookData[a][1],"/",bookData[a][5],"/", bookData[a][6],"\n")
        TotalWholesale += bookData[a][5] * bookData[a][6]
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
    while a < int(len(bookData)):
        print(b, "." ,bookData[a][0],"/", bookData[a][1],"/",bookData[a][5],"/", bookData[a][7],"\n")
        TotalRetail += bookData[a][5] * bookData[a][7]
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
    QuantityList = sorted(bookData, key=operator.itemgetter(5), reverse=True)
    a = 0
    b = 1
    while a < int(len(QuantityList)):
        print(b, "." ,QuantityList[a][0],"/",QuantityList[a][1],"/",QuantityList[a][5],"\n")
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
    CostList = sorted(bookData, key=operator.itemgetter(6), reverse=True)
    a = 0
    b = 1
    while a < int(len(CostList)):
        print(b, "." ,CostList[a][0],"/",CostList[a][1],"/",CostList[a][5],"/",CostList[a][6],"\n")
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
    AgeList = sorted(bookData, key=operator.itemgetter(4), reverse=True)
    a = 0
    b = 1
    while a < int(len(AgeList)):
        print(b, "." ,AgeList[a][0],"/",AgeList[a][1],"/",AgeList[a][5],"/",AgeList[a][4],"\n")
        a += 1
        b += 1### FIGURE OUT HOW TO SORT DATE ###

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
        while not found and index < len(bookData):
            if bookData[index][0] == searchTitle:
                found = True
            else:
                index += 1

        if not found:
            print("Book not found in the Book Inventory.")
            # Does the user want to process another transaction?
            again = input( "Process another transaction? (Y/N) ")
            continue
      
        # Get the ISBN number
        isbn = bookData[index][1]

        # Get the title
        title = bookData[index][0]

        # Get the price
        price = int(bookData[index][7])

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
bookData.append(["Introducing Python", "978-1-4493-5936-2", "Bill Lubanovic", "O'Reilly Media, Inc.", "11-24-2014", 25, 39.95, 50.00])
bookData.append(["Pro Python", "978-1-4842-0335-4", "J. Burton Browning, Marty Alchin", "Apress", "6-24-2014", 25, 35.50, 49.99])
bookData.append(["Information Technology Project Management", "978-1-2854-5234-0", "Kathy Schwalbe", "Cengage", "11-6-2015", 25, 100.25, 179.00])
bookData.append(["Starting Out with C++: From Control Structures through Objects", "978-0-1337-6939-5", "Tony Gaddis", "Cengage", "11-6-2015", 15, 105.00, 175.00])

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
        print("Leaving the Book Inventory Program")
