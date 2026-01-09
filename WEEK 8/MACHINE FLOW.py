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







