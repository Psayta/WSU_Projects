# Programming Assignment 8
# Fourth and Fifth Module
# 4.)Highest to Lowest
# 5.)Lowest to Greatest

gas_list = open('GasPrices.txt', 'r');
price_date ={}
for e in gas_list:
    e=e.split(":")
    e[1]=e[1].strip('\n')
    price_date[e[1]]=e[0]
    sorted_prices = sorted(price_date)

def high_low():
    with open ('HightoLow.txt','w') as f:
        for i in sorted_prices:
            f.write(price_date[i]+':'+i+'\n')

def low_high():
    with open ('LowtoHigh.txt','w') as f:
        for i in sorted_prices:
            f.write(price_date[i]+':'+i+'\n')
        sorted_prices.sort(reverse = True)

print ('The files have been sorted')

low_high()
high_low()

