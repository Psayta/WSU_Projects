# Programming Assingment 8
# Second Module: Average Price Per month
STARTING_MONTH = 1
ENDING_MONTH = 12

def get_price(str):
    items = str.split(':')
    return float(items[1])

def get_month(str):
    items = str.split(':')
    date_items = items[0].split('-')
    return int(date_items[0])

def get_monthly_average(gas_list, month):
    total = 0
    count = 0
    for e in gas_list:
        if get_month(e) == month:
            total += get_price(e)
            count += 1
    average = total / count
    return average

def main():
    gas_file = open('GasPrices.txt', 'r')
    gas_list = gas_file.readlines()
    for i in range(STARTING_MONTH, ENDING_MONTH + 1):
        print('The average price in Month ', i,
              '/12 was $', format(get_monthly_average(gas_list, i), '.2f'),
              sep = '')
    
main()
