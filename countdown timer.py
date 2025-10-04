 import time

my_timer = int(input("Enter the time in seconds: "))

for x in range(my_timer, 0, -1):  # countdown from my_timer to 1
    print(x)
    time.sleep(1)  # wait 1 second after each number

print("Get ready for school!")