class Procedure:

    def __init__(self, ProName, ProDate,
                 Practitioner, Charges):
        self.__ProName = ProName
        self.__ProDate = ProDate
        self.__Practitioner = Practitioner
        self.__Charges = Charges 

    def ProName(self,ProName):
        self.__ProName = ProName
    def ProDate(self, ProDate):
        self.__ProDate = ProDate
    def Practitioner(self, Practitioner):
        self.__Practitioner = Practitioner
    def Charges(self, Charges):
        self.__Charges = Charges

    def Get_ProName(self):
        return self.__ProName
    def Get_ProDate(self):
        return self.__ProDate
    def Get_Practitioner(self):
        return self.__Practitioner
    def Get_Charges(self):
        return self.__Charges 
