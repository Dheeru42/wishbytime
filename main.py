import time
timestamp = time.strftime("%H %M")
name = "RAM"
hour = int(time.strftime("%H"))
if(hour < 12):
    print(f"Good Morning {name} Sir")
elif(hour > 12):
    print(f"Good AfterNoon {name} Sir")