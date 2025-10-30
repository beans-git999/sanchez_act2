SimpleATMMachineDatabase = [
    {
        "Name": {
            "FirstName": "Ben",
            "LastName": "Ten"
        },
        "AccountNumber": 9876,
        "PIN": 6789,
        "ControlNumber": 89
    },
    {
        "Name": {
            "FirstName": "Randel",
            "LastName": "Blancakes"
        },
        "AccountNumber": 545450,
        "PIN": 8369,
        "ControlNumber": 89
    },
]

myName = input("Please enter your name: ")
myAccountNumber = input("Please Enter Your Account Number: ")
PIN = input("Please Enter Your PIN Number: ")

#for next meeting
print(f'This is your Balance : {SimpleATMMachineDatabase[1]["Balance"]}')
