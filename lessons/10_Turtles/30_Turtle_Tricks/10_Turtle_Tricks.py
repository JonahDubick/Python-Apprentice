"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
turtle
tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape("turtle")
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.forward(50)
tina.360/(50)                    # Close the window when we click on it

tina.left(360/3)
tina.forward(50)
tina.right(50)
tina.left(360/3)
turtle.exitonclick()                    # Close the window when we click on it
