#####################################################
# CMPSC 122 - Intermediate Programming
# Midterm Exam - Coding
#
# This part of the Midterm is worth 50 total points.  5 Points are
# for the code runs error free and the remaining points are detailed below.
#
# Use this code to solve the problems list below.  Each problem will
# have a # and description of what I want you to do.
#
# Program Description: 
# This program will feature a class dealing with house information.
# The user will input data and the program will output the details after.
#
# Student Name: Shane Hagan
#
#####################################################


#####################################################
# Problem #1: Create a Class that will store the
# address of the house and the year built. Call the
# Class HouseInfo.
# The to_string function is already created.  See that
# for the names of the attributes
# (10 Points)
#####################################################
class HouseInfo:
    '''Will store the adress of the house and year built'''
    def __init__(self, address, year):
        self.address = address
        self.year = year
        
    def to_string(self):
        return "The house at {0} was built in {1}.".format(self.address, self.year)

class House:
    ''' The rectangle represents the house '''

    def __init__(self, houseInfo, width=0, length=0):
        self.__width = width
        self.__length = length
        self.__houseInfo = houseInfo

    def getWidth(self):
        return self.__width

    def setWidth(self, w):
        self.__width = w

    def getLength(self):
        return self.__length

    def setLength(self, l):
        self.__length = l

    #####################################################
    # Problem #2: Create a function to set and get the
    # houseInfo Object. The address and year should be
    # passed into the set function. Both values (address
    # and year) are required fields.
    # (10 Points)
    #####################################################
    def getInfo(self):
        return self.__houseInfo
    def setInfo(self, address, year):
        self.address = address
        self.year = year
    
#####################################################
# Main Program
#####################################################

houseWidth = float(input("In feet, how wide is your house: "))
houseLength = float(input("In feet, how long is your house: "))

address = input("What is the address for your house: ")
year = input("What year was the house built: ")

#####################################################
# Problem #3: Create the HouseInfo and House objects
# based on the data entered above. Name them houseInfo
# and house, respectfully.
# (10 Points per Object)
#####################################################
HouseInfo = HouseInfo(address, year)
house = House(HouseInfo, houseWidth, houseLength)

#####################################################
# Problem #4: Use the HouseInfo's to_string to output
# the HouseInfo data.
# (5 Points)
#####################################################
print(HouseInfo.to_string())
print("The house is {0} x {1}".format(house.getWidth(), house.getLength()))
print("That is a Sq Ft of {0}.".format(house.getWidth() * house.getLength()))
