#function
#builtin
#user defined function

def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)

a = 25
b = 74
get_the_sum(a, b)

a = 88
b = 55
get_the_sum(a, b)

a = 9
b = 10
get_the_sum(a, b)

#parameter and return
def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)
    return sum
a = 25
b = 74
c = 45
d = 96

print(get_the_sum(a, b) + get_the_sum(c, d))