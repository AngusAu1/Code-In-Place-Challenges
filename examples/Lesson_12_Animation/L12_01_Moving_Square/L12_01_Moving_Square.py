# Moving Square

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

# You may need to download the graphics.py to your local folder and then import it
# graphics.py should be in the same folder of your .py, Python will find it

from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
VELOCITY = 2            # VELOCITY  = 2 is the speed to move 2 pixels each frame
DELAY = 0.01            # DELAY 1/100, it is about the time delay 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = 0
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2               # calc the mid point of y
    square = canvas.create_rectangle(start_x, start_y,
                    SQUARE_SIZE,
                    start_y + SQUARE_SIZE)
                    
    while (start_x + SQUARE_SIZE / 2) < (CANVAS_WIDTH / 2):     # when the while loop meet the mid point of the canvas (CANVAS_WIDTH / 2), then stop
        start_x += VELOCITY                                     # the start_x will be +2 (Velovity) on every while loop, in order to renew the start_x
        print("x:", start_x)
        canvas.moveto(square, start_x, start_y)                 # moveto(), it used to move the object on each loop
        time.sleep(DELAY)
        
    print("Done!")

if __name__ == '__main__':
    main()