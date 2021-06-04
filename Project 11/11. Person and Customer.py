import customer

name = input('Name: ')
address = input('Address: ')
phone = input('Phone: ')
Cnumber = input('Customer Number: ')
mail = input('Add to mailing list (y or n): ')

if mail.lower() == 'y':
    mailing_list = True
else:
    mailing_list = False

Customer = customer.Customer(name, address, phone, customer_number, mailing_list)

print('Customer Information')
print('--------------------')
print('Name: ', Customer.get_name())
print('Address: ', Customer.get_address())
print('Phone: ', Customer.get_phone())
print('Customer Number: ', Customer.get_Cnumber())
print('Mailing List: ', Customer.get_Mlist())
