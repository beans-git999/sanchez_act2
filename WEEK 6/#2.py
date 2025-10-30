colorA = ["maroon", "maroon", "red", "blue", "grey"]
colorB = ["brown", "magenta", "magenta", "cream", "white"]
colorC = ["silver", "gold", "silver", "violet", "orange"]

colorWheel_list = [colorA, colorB, colorC]
print(colorWheel_list)
print(colorWheel_list[2])
print(colorWheel_list[2][1])

colorWheel_list_Plus = colorA + colorB + colorC
print(colorWheel_list_Plus)

colorA.extend(colorB)
colorB.extend(colorC)       
print(colorA)

