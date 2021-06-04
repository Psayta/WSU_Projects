import customer

print('Order Processing') 
mail = input('Subscribe to Mailing List (Yes or No): ')
print()

if mail.lower() == 'y':
    mailing_list = True
else:
    mailing_list = False

Customer = customer.Customer('Phelan', 'WSU Vancouver',
                             '360-123-4567','11480639', mail)

print('Customer Information')
print('--------------------')
print('Name: ', Customer.get_name())
print('Address: ', Customer.get_address())
print('Phone: ', Customer.get_phone())
print('Customer Number: ', Customer.get_customer_number())
print('Mailing List: ', Customer.get_mailing_list())
print('--------------------')
print ('Order Completed') 
