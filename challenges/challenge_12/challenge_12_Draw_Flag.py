from graphics import Canvas
import random


# define the Canvas width and height
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

# define the coordinates for the rectangle 
# left top: (left_x, top_y)
# right bottom: (right_x, bottom_y)
left_x = 0
top_y = 0
right_x = CANVAS_WIDTH
bottom_y = CANVAS_HEIGHT // 2
color = 'Red'

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    rect = canvas.create_rectangle(
    left_x, 
    top_y, 
    right_x, 
    bottom_y,
    color
)
    

if __name__ == '__main__':
    main()