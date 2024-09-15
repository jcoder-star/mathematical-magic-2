from math import sqrt
number = int(input("enter the number here:"))

if number > 1:
    #check if the number is divisible by 2
    for x in range( 2, int(sqrt(number)) +1):
        if (number % x ) == 0:
            print("this is not a prime number")
            break
        else:
            print("this is a prime number")