#function with no parameters and no return
import time

def print_count_down():
    for i in range(100, 0, -1):
        time.sleep(0.5)
        print(i)

print_count_down()
