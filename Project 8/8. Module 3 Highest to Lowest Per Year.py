# Programming Assignment 8
# Third Module: Highest and Lowest Per Year
STARTING_YEAR = 1993
ENDING_YEAR = 2013

def get_price(str):
    items = str.split(':')
    return float(items[1])

def get_year(str):
    items = str.split(':')
    date_items = items[0].split('-')
    return int(date_items[2])

def get_yearly_high(gas_list, year):
    total = 0
    count = 0
    for e in gas_list:
        if get_year(e) == year:
            total += get_price(e)
            count += 1
    average = total / count
    return average
        

def main():
    gas_file = open('GasPrices.txt', 'r')
    gas_list = gas_file.readlines()
    for i in range(STARTING_YEAR, ENDING_YEAR + 1):
        print('The highest price in ', i,' was $',
              format(get_yearly_high(gas_list, i),'.2f'),sep = '')
        print (gas_list)
main()
