strFullName = "Vince Sanchez"

#upper
strNewValue = strFullName.upper()
print(strNewValue)

#count
strNewValue = strFullName.count("a")
print(strNewValue)

#split
strNewValue = strFullName.split(" ")
print(strNewValue)
strNewValue = strFullName.split("e")
print(strNewValue)
strNewValue = strFullName.split("anc")
print(strNewValue)

#replace
strNewValue = strFullName.replace("Vince", "Kobe Bean")
print(strNewValue)

#join
strFirstName = "Vince"
strMiddleName = "Manansala"
strLastName = "Sanchez"
strFullName = "-".join([strFirstName, strMiddleName, strLastName])
print(strFullName)
strFullName = strFirstName + "-" + strMiddleName + "-" + strLastName
print(strFullName)

#TF
newValue = strFullName.isnumeric()
print(newValue)

#substring
newValue = strFullName[1:9]
print(newValue)
newValue = strFullName[1:9:1]
print(newValue)

#index
print(strFullName.index("a"))
print(strFullName.index("a", 1,9))

print("vin" in strFullName)


