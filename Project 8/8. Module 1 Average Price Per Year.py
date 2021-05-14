#Programming Assignment 8
# First Module:	Average Price Per Year
# Named constants
STARTING_YEAR = 1993
ENDING_YEAR = 2013
STARTING_MONTH = 1
ENDING_MONTH = 12 

def get_price(str):
    # Split the string at the colon.
    items = str.split(':')
    # Return the price, as a float.
    return float(items[1])

def get_year(str):
    # Split the string at the colon.
    items = str.split(':')
    # Split the date item at the hyphens.
    date_items = items[0].split('-')
    # Return the year, as an int.
    return int(date_items[2])

def get_month(str):
    items = str.split(':')
    date_items = items[0].split('-')
    return int(date_items[2])
        
def get_yearly_average(gas_list, year):
    # Initialize an accumulator.
    total = 0
    # Initialize a counter.
    count = 0
    # Step through the string, getting the sum of all the prices
    # for the specified year.
    for e in gas_list:
        if get_year(e) == year:
            total += get_price(e)
            count += 1
    # Calculate the average.
    average = total / count
    # Return the average.
    return average

def get_monthly_average(gas_list, month):
    total = 0
    count = 0
    for e in gas_list:
        if get_month(e) == month:
            total += get_price(e)
            count += 1
    average = total / count
    # Return the average.
    return average


def main():
    # Open the file.
    gas_file = open('GasPrices.txt', 'r')
    # Read the file's contents into a list.
    gas_list = gas_file.readlines()
    # Display the average price for each year.
    for i in range(STARTING_YEAR, ENDING_YEAR + 1):
        print('///////////Average Price Per Year///////////////')
        print('The average price in ', i,
              ' was $', format(get_yearly_average(gas_list, i), '.2f'),
              sep = '')
        print('///////////Average Price Per Month///////////////')
        print('The average price in ', i,
              ' was $', format(get_monthly_average(gas_list, i), '.2f'),
              sep = '')
    
main()
