colorA = ("maroon", "maroon", "red", "blue", "grey")
print(colorA)
print(colorA.index("grey"))
print(colorA.count("maroon"))
print(colorA[4])


colorB = ("green", "orange", "white", "purple")
colorWheel = (colorA, colorB)
print(colorWheel)

Superlist = [ {1, 2, 3}, True, colorWheel, ["a"], [True, False, 232.232]]

mytuple = (
    (1, 2, 3, "A"),
    (4, 5, 6, "B"),
    (7, 8, 9, "C"),
    (0, "*", "#", "D"),
)

print(mytuple[3][2])

