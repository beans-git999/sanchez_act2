
strInput = "214vin94539309ce214 32san02930294893820c208402h012390293e02z02"
print(strInput.replace("214",""))

newString = ""
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)


