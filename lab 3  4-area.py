import math
t_peri = lambda p,q,r : p + q + r
r_area = lambda len, ht : len*ht
s_area = lambda a : a*a*a*a

print("Perimeter of Triangle (10,20,15) is:", t_peri(10,20,15))
print("Area of Rectangle (30,20) is:", r_area(30,20))
print("Area of Square (2) is:", s_area(2))