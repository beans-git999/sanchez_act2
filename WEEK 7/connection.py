import time
isConnected = "No"

for retry in range(4):
    time.sleep(2)
    isConnected = input("Bluetooth device ready to pair?")

    if isConnected == "yes":
        print("Now Connected")
        break
    else:
        print("Request timed out.")

print("Processing your request . . .")
