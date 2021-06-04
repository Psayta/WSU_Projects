#Programming Assignment 12

def main():
    num = int(input('Enter a number between 1 and 50: '))
    print('You inputted', num, 'the sum from that number equals,', SumofNumbers(num))

def SumofNumbers(num):
    if num <= 1:
        return num
    else:
        return num + SumofNumbers(num-1)


main()



