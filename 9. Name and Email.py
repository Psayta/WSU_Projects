# Programming Assignment #9
# Name and Email Addresses
import pickle 

LOOK_UP =1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    emails = {}
    choice = 0

    while choice != QUIT:
        choice = menu_choice()

        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)
            
def menu_choice():
    print()
    print('Name and Email Addresses')
    print('---------------------------')
    print('1. Look up a Email')
    print('2. Add a new Email')
    print('3. Change a Email')
    print('4. Delete a Email')
    print('5. Quit the Email')
    print('---------------------------')

    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

def look_up(emails):
    emails = pickle.load(open('emails.dat', 'rb'))
    name = input('Enter a name: ')
    print('------------------------')
    print(emails.get(name, 'Not found.'))
    print('------------------------')
        
def add(emails):
    name = input('Enter a name: ')
    email = input('Enter an email: ')
    print('------------------------')
    if name not in emails:
        emails[name] = email
        pickle.dump(emails, open('emails.dat', 'wb'))
    else:
        print('That entry already exists.')
    print('------------------------')
    
def change(emails):
    name = input('Enter a name: ')
    print('------------------------')
    if name in emails:
        email = input('Enter the new email: ')
        emails[name] = email
        pickle.dump(emails, open("emails.dat", "wb"))
    else:
        print('That name is not found.')
    print('------------------------')

def delete(emails):
    name = input('Enter a name: ')
    print('------------------------')
    if name in emails:
        del emails[name]
    else:
        print('That name is not found.')
    print('------------------------')

main()

        
                 
