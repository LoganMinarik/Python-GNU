# The variable named number contains a value entered by the user,
# which occurred earlier in the program.
# (For now, do not worry about what "def" means -- this is defining
# a function, which we will learn about soon... we need it here in order
# to get the auto-grader to give you feedback)
def result(number):
    # divide the variable number by 2, and store the result in a new variable
    # named answer
    answer = number / 2

    # then, add 40 to the previous result, storing the result in the variable answer 
    answer = answer + 40

    # do not change this line (it is needed for the autograder) 
    return answer 

# This line of code allows you to test your answer when you click the Run button
print(result(4))
# Note that the autograder will try other numbers than just this one!