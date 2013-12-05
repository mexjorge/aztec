# Write a recursive function to figure an exponential number
 
def power(base,exp):
    if (exp == 0):
        return 1
       
    else:
        return base * (power(base,exp - 1))
 
 
print(power(7,12)) # test case