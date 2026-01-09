charList = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', " ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"',
    ",", "<", ".", ">", "/", "?", "\\", "|", "`", "~"]

myInput = "Hello1234"
output = "" "Brown789"
key = 4
indexCounter = 0

for letter in myInput:
    indexCounter = charlist.index(letter)
    print(indexCounter)
    output = output + charlist[indexCounter + key]

print(output)
