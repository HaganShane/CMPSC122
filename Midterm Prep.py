################################
# Exam Prep
################################

class Assignment:
    ''' An assignment has a type, score and max points '''
    def __init__(self, assignType, score, maxPts):
        self.__type = assignType
        self.__score = score
        self.__maxPts = maxPts

    def getType(self):
        return self.__type

    #############################
    # Problem #1
    # Create a function that returns the
    # % based on the score / max
    #############################
    def getPercentage(self):
        return score / maxPts
    
class CourseAssignments:
    ''' Stores the assignments for the course '''
    #############################
    # Problem #2
    # Create the init function.
    # Inside this, create a private
    # list called assignments
    #############################
    def __init__(self):
        self.__assignments = []

    def addAssignment(self, assignment):
        self.__assignments.append(assignment)

    def averageAssignment(self, t):
        count = 0
        sum = 0
        #############################
        # Problem #3
        # Create a loop that goes thru
        # the list and checks for the type
        # if it is the type, add the percentage
        # to the sum
        #############################
        for s in self.__assignments:
            if t == s.getType():
                count += 1
                sum += s.getPercentage()
        
        return sum / count

course = CourseAssignment()
for x in range (10):
    t = int(input("Enter a Assignment Type (1, 2, or 3): "))
    #############################
    # Problem #4
    # Prompt the user to enter the score
    # and max points
    #############################
    score = int(input("Enter the score: "))
    maxpts = int(input("Enter the max points: "))

    #############################
    # Problem #5
    # Create a new Assignment object
    #############################
    assignment = CourseAssignment()

    #############################
    # Problem #6
    # Add the new assignment to the Course
    #############################
    assignment += course

