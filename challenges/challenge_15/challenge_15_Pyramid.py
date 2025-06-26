from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


    for j in range(BRICKS_IN_BASE):
        
        # starting_pt is the starting point for the left_x
        # Since the requirement is the pyramid should be at the centered
        # of the bottom, so it needed to calc the starting pt that the 1st brick
        # Thus, the starting pt = (the Canvas width - the length of total no. of the bricks)/2 
        # the length of total no. of the brick = Brick width * no of bricks
        # and therefore for the 1st row (when no of brick is 14), the length is 30 * 14 = 420
        # However, since the no of bricks in each row decreases by one
        # we control that by a for loop with j
        # Thus, when the outter for loop begin, j = 0, and then j = 1...
        # And the BRICKS_IN_BASE will be decreased by 1 each loop

        starting_pt = int((CANVAS_WIDTH - (BRICK_WIDTH * (BRICKS_IN_BASE - j))) / 2)
        # print(starting_pt) # 90 -> 105 -> 120 ..., used for testing purpose

        # it is the 2nd for loop with i, to draw each row of bricks
        
        # left_x = starting_pt + (BRICK_WIDTH * i)
        # starting_pt will be re-calc for each new row, based on starting_pt = int((CANVAS_WIDTH - (BRICK_WIDTH * (BRICKS_IN_BASE - j))) / 2)
        # Brick width is started from 0, and then increase by 30 on every new row

        # top_y  = CANVAS_HEIGHT - (BRICK_HEIGHT * (j + 1))
        # Actually it is a constant value on every each row
        # the Brick height is start by 12 will be increase by 12 on every new row

        # right_x = starting_pt + (BRICK_WIDTH * (i + 1))
        # starting_pt will be re-calc for each new row, based on starting_pt = int((CANVAS_WIDTH - (BRICK_WIDTH * (BRICKS_IN_BASE - j))) / 2)
        # Brick width is started from 30, and then increase by 30 on every new row

        # bottom_y  = CANVAS_HEIGHT - (BRICK_HEIGHT * j)
        # Actually it is a constant value on every each row
        # the Brick height is start by 0 will be increase by 12 on every new row


        for i in range(BRICKS_IN_BASE - j):
            left_x = starting_pt + (BRICK_WIDTH * i)
            top_y = CANVAS_HEIGHT - (BRICK_HEIGHT * (j + 1))

            right_x = starting_pt + (BRICK_WIDTH * (i + 1))
            bottom_y = CANVAS_HEIGHT - (BRICK_HEIGHT * j)

            # Draw the rectangle, by defined (left_x, top_y) & (right_x, bottom_y)
            # with the black outline and yellow color filling in
            canvas.create_rectangle(
            left_x, top_y, 
            right_x, bottom_y, 
            "yellow", "black"
            )
        
        # Control the next for loop to decending by 1
        # Which means BRICK_IN_BASE: 14 -> 13 -> 12 -> ...
        j -= 1 # j = j -1
        

"""
    canvas.create_rectangle(
    0, CANVAS_HEIGHT - BRICK_HEIGHT, 
    BRICK_WIDTH, CANVAS_HEIGHT, 
    "yellow", "black"
    )
"""    

if __name__ == '__main__':
    main()