""""
This is a calcultor which performs simple
calculations as given as an input by user.
"""

print("You can quit the program by entering 'q' button.")
while(True):
    exp = input("Enter an expression: ")
    if(exp != 'q'):
        print(eval(exp))
    else:
        break