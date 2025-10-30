colorA = {"maroon", "maroon", "red", "blue", "grey"}
colorB = {"brown", "magenta", "maroon", "cream", "blue"}
print(colorA)
colorA.add("purple")
print(colorA)

colorUnion = colorA.union(colorB)
print(colorUnion)
colorIntersection = colorA.intersection(colorB)
print(colorIntersection)
colorDifference = colorA.difference(colorB)
print(colorDifference)

colorA = {"maroon", "maroon", "red", "blue", "grey"}
colorB = {"brown", "magenta", "maroon", "cream", "blue"}
colorFusionListOfSet = [colorA, colorB]
print(colorFusionListOfSet)

