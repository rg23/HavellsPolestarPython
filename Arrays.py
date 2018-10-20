import turtle # Allows us to use turtles

def printPattern():
    i = 0
    for i in range(1,25):
        print(i)
        alex.forward(5)  # Tell alex to move forward by 50 units
        alex.left(15)  # Tell alex to turn by 90 degrees
        alex.forward(5)  # Complete the second side of a rectangle
        alex.right(3)  # Tell alex to turn by 90 degrees right

        # if i % 20 == 0:
        #     alex.forward(5)  # Tell alex to move forward by 50 units
        #     alex.right(15)  # Tell alex to turn by 90 degrees
        #     alex.forward(5)  # Complete the second side of a rectangle
        #     alex.left(3)  # Tell alex to turn by 90 degrees right

    return

window = turtle.Screen() # Creates a playground for turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
x=0
y=0
i=0
for i in range(10):
    if i%2==0:
        alex.pen(fillcolor="pink", pencolor="red", pensize=8)
    else:
        alex.pen(fillcolor="green", pencolor="green", pensize=8)
    if(i<5):
        y=y-20
        alex.setpos(x,y)
        printPattern()
    else:
        y=0
        x=x-20
        alex.setpos(x,y)
        printPattern()

window.mainloop() # Wait for user to close window