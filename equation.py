import math 
a = float(input("Write the first number : "))
b = float(input("Write the second number : "))
c = float(input("write the third number : "))
delta = pow( b , 2 ) - 4 * a * c
if delta < 0 :
    print ("The equation has no real roots")
elif delta == 0 :
    print("The equation has one real root : " , -b / ( 2 * a ))
elif delta > 0 :
    x1=(-b + math.sqrt(delta))/(2*a)
    x2=(-b - math.sqrt(delta))/(2*a)
    print ("The first real root is : " , x1 , "The second real root is : " , x2)