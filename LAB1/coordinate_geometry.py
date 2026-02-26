import math
x1 = float(input("please enter the x1 value : "))
y1 = float(input("please enter the y1 value : "))
x2 = float(input("please enter the x2 value : "))
y2 = float(input("please enter the y2 value : "))

distance = math.sqrt(x2-x1)**2 + (y2-y1)**2
print("Distance is : " + str(distance))
