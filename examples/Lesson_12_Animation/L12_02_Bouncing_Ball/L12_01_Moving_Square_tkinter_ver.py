# Moving Square

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

# You may need to download the graphics.py to your local folder and then import it
# graphics.py should be in the same folder of your .py, Python will find it

import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    window = tk.Tk()
    canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()   # add the canvas into a window

    square = canvas.create_rectangle(0, 180, 40, 220, fill='blue')

    def move():
        nonlocal square                 # tell Python, the variable square is defined at main(), not defined inside move()
        for x in range(180):            # for loop 180 times
            canvas.move(square, 1, 0)   # tkinter haven't moveto(), and moveto() is absolute move, but move() is relative move
            window.update()             # refresh window on each time looping, if the code without "window.update()", then tkinter will wait the for loop complated and then refresh window, and therefore the animation will not work
            canvas.after(5)             # delay 5ms and then go into next for loop

    move()
    window.mainloop()   # very important on tkinter, if there is no window.mainloop(), the window will close immediately;
                        # which means it keep the window active until user close the window

if __name__ == '__main__':
    main()