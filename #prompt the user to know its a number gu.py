#prompt the user to know its a number guessing game
print('I am thinking of a number')
guess = int(input("What is it? :"))
#did they gues correctly if so say "Great"
if guess == 42:
    print("You're Correct")
#if not say too bad
if guess != 42:
    print("You're Incorecct!!!!")