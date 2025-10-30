import math

myIntegerA = 237
myIntegerB = 190
myIntegerC = 10
myFloatA = 25.45
myFloatB = 14.55
myComplexA = 25 - 3j
myComplexB = 10 - 12j
#+, -, /, *
summation = myIntegerA + myIntegerB
print(summation)
myDiff = myIntegerA - myIntegerB
print(myDiff)
product = myIntegerA * myIntegerB
print(product)
quotient = myIntegerA / myIntegerB
print(quotient)
roundquotient = round(quotient, 3)
remainder = myIntegerA % myIntegerB
print(remainder)
remainder = myIntegerB % myIntegerC
print(remainder)
#GEMDAS
myComProduct = myComplexA * myComplexB
print(myComProduct)
print(3*2*1)
print(math.factorial(3))
print(math.radians(math.cos(math.degrees(90))))
cos_90_deg = math.tan(math.radians(45))
print(cos_90_deg)

