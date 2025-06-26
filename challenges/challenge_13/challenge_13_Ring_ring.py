from graphics import Canvas

CANVAS_WIDTH = 150
CANVAS_HEIGHT = 150

# the diameter of the outer red circle
OUTER_DIAMETER = 50

# the left and top corrdinates of the outer red circle
OUTER_LEFT_X = (CANVAS_WIDTH - OUTER_DIAMETER)/2
OUTER_TOP_Y = (CANVAS_HEIGHT - OUTER_DIAMETER)/2

# the size of the red band of the ring
# inner_left_x = outer_left_x + RING_WIDTH
RING_WIDTH = 10

INNER_LEFT_X = OUTER_LEFT_X + RING_WIDTH
INNER_TOP_Y = OUTER_TOP_Y + RING_WIDTH


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_oval(OUTER_LEFT_X, OUTER_TOP_Y, 
                        OUTER_LEFT_X + OUTER_DIAMETER, 
                        OUTER_TOP_Y + OUTER_DIAMETER, "red")

    #canvas.create_oval(INNER_LEFT_X, INNER_TOP_Y, 90, 90, "White")

   
    canvas.create_oval(INNER_LEFT_X, INNER_TOP_Y, 
                        INNER_LEFT_X + OUTER_DIAMETER - RING_WIDTH*2, 
                        INNER_TOP_Y + OUTER_DIAMETER - RING_WIDTH*2, "White")
   
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
    