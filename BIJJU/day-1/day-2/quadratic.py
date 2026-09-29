import math
a = float(input("enter the value"))
b = float(input("enter the value"))
c = float(input("enter the value"))

d = b**2 - 4*a*c

x1 = (-b + math.sqrt(d))/(2*a)
x2 = (-b - math.sqrt(d))/(2*a)

print("root of x1 : {x1}")
print("root of x2 : {x2}")