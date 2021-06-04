# Programming Assignment 11 

class Person:
    #initializer 
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    # Mutators 
    def name(self, name):
        self.__name = name
    def address(self, addresss):
        self.__address = address
    def phone(self, phone):
        self.__phone = phone
    # Accessors 
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_address(self):
        return self.__address 

class Customer(Person):
    #initializer
    def __init__(self, name, address,
                 phone, Cnumber, Mlist):
        Person.__init__(self, name, address, phone)
        self.__Cnumber = Cnumber
        self.__Mlist = Mlist
    # Mutators 
    def customer_number(self, Cnumber):
        self.__Cnumber = Cnumber
    def mailing_list(self, Mlist):
        self.Mlist = Mlist
    # Accessors 
    def get_customer_number(self):
        return self.__Cnumber
    def get_mailing_list(self):
        return self.__Mlist



