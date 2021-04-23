#Test Averages and Grades
#Inputs 
Test1 = float(input("Enter Test Score 1: "))
Test2 = float(input("Enter Test Score 2: "))
Test3 = float(input("Enter Test Score 3: "))
Test4 = float(input("Enter Test Score 4: "))
Test5 = float(input("Enter Test Score 5: "))
#Functions
#Calculates the average score of the inputs of all five tests
def calc_average():
    AvgScore=(Test1+Test2+Test3+Test4+Test5)/5 
    print ("Your Average Score is:" ,(AvgScore))
#Takes a Test score and gives a grade based on the argument
def determine_grade():
    TS = float(input("Input one of the test scores for a grade:"))
    if TS >= 90:
        print("Test Score is an A")
    elif TS <= 89 and TS >= 80:
        print("Test Score is an B")
    elif TS <= 79 and TS >= 70:
        print("Test Score is an C")
    elif TS <= 69 and TS >= 60:
        print("Test Score is an D")
    elif TS <= 59:
        print("Test Score is an F") 

#Called upon Functions
calc_average()
determine_grade()
