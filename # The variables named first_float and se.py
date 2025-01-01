# The variables named first_float and second_float contain values entered 
# by the user, which were converted to floating point numbers 
# (For now, do not worry about what "def" means -- this is defining  
# a function, which we will learn about soon... we need it here in order  
# to get the auto-grader to give you feedback)  
def smallest(first_float, second_float):  
    # what code is needed to determine what the smallest number is?  
    # HINT: you can solve this using two if statements  
    
    # ADD YOUR CODE HERE  
    if first_float < second_float:
        result = first_float
    if second_float < first_float:
        result = second_float

    if first_float == second_float:
        result = first_float
    # do not modify the following line  
    return result 

# the following line of code allows you to run your program and test it
print('The smallest number is', smallest(53.2, 100.3))
print('The smallest number is', smallest(1.0, 42.0))
print('The smallest number is', smallest(2.0, 2.0))