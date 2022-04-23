# Write a python function to check if number is prime or not 

"""Whats a prime number? 
"""

print("Checking if number is prime or Not")


y=int(input ("Enter a number to check:"))
if y>1:
    for i in range (2, y//2):
        if (y%1)==0:
            print(y, "is not a prime number")
        break
    else:
        print (y, "is a prime number")
else:
    print(y, "is neither prime nor composite")     




# write python function that when yous the function you have created 
# checks wether the number belongs to fibonacci sequency or not