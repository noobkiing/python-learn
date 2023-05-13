# A Tuple is used when you have values in pair and are immutable (aren't going to change)
coordinaate=(29.0,34.0)
def return_two_values():
    return 1, 2
    
a, b = return_two_values()
print(a)   # Output: 1
print(b)   # Output: 2
#In this example, the function return_two_values() returns a tuple containing the values 1 and 2.
#The tuple is automatically unpacked into the variables a and b when the function is called.