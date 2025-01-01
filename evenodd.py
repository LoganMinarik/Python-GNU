# The variable named number contains a value entered by the user,  
# which was converted to an integer and stored in the variable named user_answer 
# (For now, do not worry about what "def" means -- this is defining  
# a function, which we will learn about soon... we need it here in order  
# to get the auto-grader to give you feedback)  
def even_or_odd(user_answer):  
    # what code is needed to determine if the answer is even or odd? 
    # HINT: use the mod % operator and two if statements 
    # store your result in the variable result 

    if user_answer % 2 == 0:
        result = 'EVEN'
    if user_answer % 2 == 1:
        result = 'ODD'
    
    # do not modify the following line 
    return result 

# the following line of code allows you to run your program and test it
print('The number 4 is', even_or_odd(4))
print('The number 3 is', even_or_odd(3))