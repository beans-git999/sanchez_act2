#no return
#function with parameters and no return
import time


def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)

a = 25
b = 74
c = 45
d = 96
get_the_sum(a, b)

#parameters return
def get_the_sum(input1, input2):
    sum = input1 + input2
    print(sum)
    return sum
a = 25
b = 74
c = 45
d = 96

print(get_the_sum(a, b) + get_the_sum(c, d))


if __name__ == '__main__':
    print_count_down()