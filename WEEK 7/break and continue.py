
print("before loop")

for i in range(10):
    if i % 4 == 0:
        print("Even Number : " + str(i))
        continue
    elif i > 6:
        print("i is greater than 6")
        break
    print("i value now is : " + str (i))

    print("after loop")