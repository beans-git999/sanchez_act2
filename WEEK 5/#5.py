
isPresent = False #boolean
isExist = True #booolean
isAvailable = "True" #boolean
isValid = 1 #integer
isOkay = 0 #integer
isNumeric = False #boolean
myChar = "5"

isNumeric = myChar.isnumeric()
strIsNumeric = str(myChar.isnumeric())
print([isNumeric])
print([strIsNumeric])
#Comparison Operator
# in, is, not in, is not
# ==, >=, >, <=, <, !=
a = 5
b = 6
isEqual = (a == b)  # False
print(isEqual)
isGTE = (a >= b)  # False
print(isGTE)
isLTE = (a <= b)  # True
print(isLTE)
#membership and identity operator
# in, not in, is, is not
isIn = (5 in [25, 45, 23, 12, 5, 27])
print(isIn)  # True
isIn = (5 in [25, 45, 23, 12, 27])
print(isIn)  # False
isIn = ("hello" in "hello world hi eath")
print(isIn)  # True
isIS = ("hello" is "hello")
print(isIS)  # True
isIS = ("hello" is "hi hello")
print(isIS)  # False

#AND OR NOT NAND NOR ------- EXOR, EXNOR

isOkay = (5 in [25, 45, 23, 12, 5, 27]) and (5 in [25, 45, 23, 12, 27])
print(isOkay) #False
isOkay = (5 in [25, 45, 23, 12, 5, 27]) or (5 in [25, 45, 23, 12, 27])
print(isOkay) #True
