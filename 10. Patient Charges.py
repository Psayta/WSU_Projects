import patients
import procedures

def Get_Patient():
    FirstName = input('Patient First Name: ')
    MiddleName = input('Patient Middle Name: ')
    LastName = input('Patient Last Name: ')
    Address = input('Patient Address: ')
    City = input('Patient City: ')
    State = input('Patient State: ')
    ZIPCode = input('Patient ZIP Code: ')
    PhoneNumber = input('Patient Phone Number: ')
    EMName = input('Patient Emergency Name: ')
    EMPhone = input('Patient Emergency Phone Number: ')

    Patients = patients.Patient(FirstName, MiddleName, LastName, Address, City,
                               State, ZIPCode, PhoneNumber, EMName, EMPhone)

    print('///////////////////////////////////////')
    print('Inputted Patient Informations: ')
    print('First Name:',Patients.Get_FirstName())
    print('Middle Name:',Patients.Get_MiddleName())
    print('Last Name:',Patients.Get_LastName())
    print('Address:',Patients.Get_Address())
    print('City:',Patients.Get_City())
    print('State:',Patients.Get_State())
    print('ZIP Code:',Patients.Get_ZIPCode())
    print('Phone Number:',Patients.Get_PhoneNumber())
    print('EMName:',Patients.Get_EMName())
    print('EMPhone:',Patients.Get_EMPhone())
    print('//////////////////////////////////////') 

def main():
    procedures = Get_Procedures()
    print('Displayed is the assigned upcomming procedures.')
    Display_Procedures(procedures) 

def Get_Procedures():
    procedure_list = [] 

    print('Enter the three procedures.')
    for i in range (1, 4):
        ProName = input('Procedure: ')
        ProDate = input('Date: ')
        Practitioner = input('Practitioner: ')
        Charges = float(input('Cost: '))
        print() 

        medprocedure = procedures.Procedure
        (ProName,ProDate, Practitioner, Charges)

        procedure_list.append(medprocedure)
        
    return procedure_list

def Display_Procedures(procedure_list): 
    for a in procedure_list: 
        print('Procedure Name: ', a.Get_ProName())
        print('Procedure Date: ', a.Get_ProDate())
        print('Practitioner: ', a.Get_Practitioner())
        print('Charges: ', a.Get_Charges())
        print()
    
        
Get_Patient()
main()
