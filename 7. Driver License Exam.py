#Programming Assignment 7: Drivers License Exam

def main(): # Main function used to list the correct answers and call other functions 
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                       'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    print('The Correct answers are as followed:',correct_answers)
    student_answers = read_answers()
    check_answers(correct_answers, student_answers)
    
def read_answers(): # Function used to read answers provided by the student 
    student_answers =[]
    file_object = open('studentanswers.txt', 'r') # Reads Student answers 
    for t in file_object:
        t = t.rstrip('\n')
        student_answers.append(t)
    return student_answers
    
def check_answers(correct_answers, student_answers): #Checks whether the answers provided are similar to the correct answer 
    count = 0
    wrong_answers = []
    print('Students Answers:' ,student_answers) #Student Answer List Printed
    for n in range(20): #Compares answer list with the student answer list and provides count of correct answers 
        if correct_answers[n] == student_answers[n]:
            count += 1
        else: #Indicates where in the list the answers were wrong 
            wrong_answers.append(n)
            count += 0
    if count >= 15: #Prints based on the number of answered correctly 
        print('Passed!')
        print('Number of Correct Answewrs', count)
        print('Number of Incorrect answers', 20 - count)
        print('The question that were wrong',wrong_answers)
    else:
        print('Failed!')
        print('Number of Correct Answewrs', count)
        print('Number of Incorrect answers', 20 - count)
        print('The question that were wrong',wrong_answers)
        
main()# Calls main function 
