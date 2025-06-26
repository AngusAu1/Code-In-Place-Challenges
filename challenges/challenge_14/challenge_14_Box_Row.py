from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

# print(BOX_SIZE)

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


    #x = CANVAS_WIDTH % N_BOXES
    # print(x) # 0
    
    for i in range(N_BOXES):
        top_y = CANVAS_HEIGHT - BOX_SIZE    # 200 - 80 = 120
        bottom_y = CANVAS_HEIGHT            # 200
        
        # For i 
        left_x = i * int(BOX_SIZE)          # 0 -> 80 -> 160 -> 240 -> 320


        right_x = (i+1) * int(BOX_SIZE)     # 80 -> 160 -> 240 -> 320 -> 400

        # For testing the cooridate of left_x and right_x
        #print("for i is " + str(i))
        #print(left_x)
        #print(right_x)

        # Creates a white rectangle 
        # with a black outline
        canvas.create_rectangle(
        left_x, 
        top_y, 
        right_x, 
        bottom_y, 
        "white", 
        "black"
        )



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    