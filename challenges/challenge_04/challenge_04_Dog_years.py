# Each year for a human is like 7.18 years for a dog

# defined the constant no as DOG_YRS_MULTIPLIER
DOG_YRS_MULTIPLIER = 7.18  

def main():
    # input the age year by end user
    # multiply the input value with the constant
    # print the result
    age_year = int(input("Enter an age in calendar years: "))
    
    dog_year = age_year * DOG_YRS_MULTIPLIER

    print("That's " + str(dog_year) + " in dog years!")



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()