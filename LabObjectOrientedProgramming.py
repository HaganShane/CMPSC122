class ScoreReport:
    '''Score Report stores student grades, averages, and letter grades'''
    def __init__(self, StudentName, StudentID, Cmpsc=0, Math=0):
        self.StudentName = StudentName
        self.StudentID = StudentID
        self.__Cmpsc = Cmpsc
        self.__Math = Math
        self.__CalculateAverage()

    def to_string(self):
        return "{0}\t\t{1}\t{2}\t{3}\t{4}\t\t{5}".format(self.StudentName, self.__Cmpsc, self.__Math, self.__Average, self.__Letter, self.StudentID)

    def __CalculateAverage(self):
        '''Calculates average of CMPSC and Math scores'''
        sum = self.__Cmpsc + self.__Math
        if self.__Cmpsc == 0 or self.__Math == 0:
            self.__Average = sum
        else:
            self.__Average = sum / 2
        self.__CalculateLetter()


    def __CalculateLetter(self):
        '''Set the letter grade based on average'''
        if self.__Average > 94:
            self.__Letter = "A"
        elif self.__Average >= 90:
            self.__Letter = "A-"
        elif self.__Average >= 87:
            self.__Letter = "B+"
        elif self.__Average >= 84:
            self.__Letter = "B"
        elif self.__Average >= 80:
            self.__Letter = "B-"
        elif self.__Average >= 77:
            self.__Letter = "C+"
        elif self.__Average >= 70:
            self.__Letter = "C"
        elif self.__Average >= 60:
            self.__Letter = "D"
        else:
            self.__Letter = "F"

    def GetCMPSC(self):
        return self.__Cmpsc

    def GetMath(self):
        return self.__Math

    def GetAverage(self):
        return self.__Average

    def GetLetter(self):
        return self.__Letter

    def SetCMPSC(self, Cmpsc):
        self.__Cmpsc = Cmpsc
        self.__CalculateAverage()

    def SetMath(self, Math):
        self.__Math = Math
        self.__CalculateAverage()

# Create an empty list
StudentReports = []
# Generate 5 score report and add to list
# Make sure 1 is using defaults, use the set functions to add data
sr1 = ScoreReport("Shane Hagan", "sdh5378", Cmpsc = 95, Math = 75)
StudentReports.append(sr1)
sr2 = ScoreReport("Random Student", "rnd123")
sr2.SetCMPSC(70)
sr2.SetMath(80)
StudentReports.append(sr2)


sr1 = ScoreReport("John Doe", "jdd5343", Cmpsc = 76, Math = 80)
StudentReports.append(sr1)
sr1 = ScoreReport("Joe Smith", "jus1234", Cmpsc = 98, Math = 56)
StudentReports.append(sr1)
sr1 = ScoreReport("Other Student", "ops4567", Cmpsc = 73, Math = 67)
StudentReports.append(sr1)

print("Student\t\t\tCMPSC\tMath\tAverage\tGrade\t\tPSU ID")
print("#" * 72)
for s in StudentReports:
    print(s.to_string())
    


    
