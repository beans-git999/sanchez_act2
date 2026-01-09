#function with no parameters and no return
import time

def print_count_down():
    for i in range(100, 0, -1):
        time.sleep(0.5)
        print(i)

print_count_down()


import time
import os

9#SIMPLE ATM MACHINE FLOW
'''''
welcome_messages():
card_reader(isCardInserted):
input_and_validate_pin_number(pinNumber): return isValid
transaction_selection(transaction):
amount_and_account_selection(amount):
transaction_validation(transaction):
amount_and_account_validation(amount, balance): return isValid
card_ejection():
cash_dispensing():
print_receipt(amount, balance):
'''

amount = 0
balance = 1000
pin_number = "000143"

def welcome_messages():
    time.sleep(1)
    print("Welcome to BANGKO SENTRAL NG ECE 1-4")
    time.sleep(1)
    print("............................")
    time.sleep(1)
    print("Please enter your card")

def card_reader(isCardInserted):
    if isCardInserted == "YES":
        print("Card is inserted")
        return True
    else:
        return False

def input_and_validate_pin_number():
    for i in range(4):
        if i == 3:
            print("Card Blocked, Pumunta ka sa Bangko")
        inputPin = input("Please enter your pin number: ")
        if inputPinNumber == pin_Number:
            return False
        else:
            print("Wrong pin, Ulitin Mo")

amount = 0
balance = 1000
pin_number = "000143"

while True:
    welcome_messages()
    isCardInserted = input("Is card inserted?")
    if not card_reader(isCardInserted): #False
        continue
    print("Next Steps")
    inputPinNumber = input("Please enter pin number")
    input_and_validate_pin_number(inputPinNumber)



#no return
#function with parameters and no return
import time


def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)

a = 25
b = 74
c = 45
d = 96
get_the_sum(a, b)

#parameters return
def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)
    return sum
a = 25
b = 74
c = 45
d = 96

print(get_the_sum(a, b) + get_the_sum(c, d))


if __name__ == '__main__':
    print_count_down()

#function
#builtin
#user defined function

def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)

a = 25
b = 74
get_the_sum(a, b)

a = 88
b = 55
get_the_sum(a, b)

a = 9
b = 10
get_the_sum(a, b)

#parameter and return
def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)
    return sum
a = 25
b = 74
c = 45
d = 96

print(get_the_sum(a, b) + get_the_sum(c, d))