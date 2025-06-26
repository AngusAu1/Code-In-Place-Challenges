"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""
# Classic for loop to loop the numbers by descending order for 10 to 1

# defined the constant i = 10, which means it started from 10
i = 10

# for loop to print and i = i -1 in each loop
def main():
    for i in range(10):
        print(10 - i)
        i -= 1
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()