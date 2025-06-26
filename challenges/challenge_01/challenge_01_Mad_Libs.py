"""
Mad Libs
Uses constants to tell a mad libs story.
"""

# Fun fact: 6174 is known as Kaprekar's constant,
# and it's a pretty mysterious number :)


# defined constant "WIZARD", "NUMBER_OF_FRUIT" &"FRUIT"
WIZARD = 'Karel'
NUMBER_OF_FRUIT = 6174
FRUIT = 'mangoes'

def main():
    # using print to display those constant with the assigned value
    print("There once was a wizard by the name of " + WIZARD + " who loved to eat " + FRUIT + ".")
    print(WIZARD + " always kept a stash of " + str(NUMBER_OF_FRUIT) + " " + FRUIT + " in their house...")

if __name__ == '__main__':
    main()