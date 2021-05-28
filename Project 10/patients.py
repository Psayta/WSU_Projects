# Programming Assignment 10

class Patient:

    def __init__(self, FirstName, MiddleName, LastName, Address,
                 City, State, ZIPCode, PhoneNumber, EMName, EMPhone):
        self.__FirstName = FirstName
        self.__MiddleName = MiddleName
        self.__LastName = LastName
        self.__Address = Address
        self.__City = City
        self.__State = State
        self.__ZIPCode = ZIPCode
        self.__PhoneNumber = PhoneNumber
        self.__EMName = EMName
        self.__EMPhone = EMPhone

    def FirstName(self, FirstName):
        self.__FirstName = FirstName
    def MiddleName(self, MiddleName):
        self.__MiddleName = MiddleName
    def LastName(self, LastName):
        self.__LastName = LastName
    def Address(self, Address):
        self.__Address = Address
    def City(self, City):
        self.__City = City
    def State(self, State):
        self.__State = State
    def ZIPCode(self, ZIPCode):
        self.__ZIPCode = ZIPCode
    def PhoneNumber(self, PhoneNumber):
        self.__PhoneNumber = PhoneNumber
    def EMName(self, EMName):
        self.__EMName = EMName
    def EMPhone(self, EMPhone):
        self.__EMPhone = EMPhone

    def Get_FirstName(self):
        return self.__FirstName
    def Get_MiddleName(self):
        return self.__MiddleName
    def Get_LastName(self):
        return self.__LastName 
    def Get_Address(self):
        return self.__Address
    def Get_City(self):
        return self.__City
    def Get_State(self):
        return self.__State
    def Get_ZIPCode(self):
        return self.__ZIPCode
    def Get_PhoneNumber(self):
        return self.__PhoneNumber
    def Get_EMName(self):
        return self.__EMName
    def Get_EMPhone(self):
        return self.__EMPhone
