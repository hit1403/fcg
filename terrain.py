import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")

# Set up the turtle
terrain_turtle = turtle.Turtle()
terrain_turtle.speed(0)  # Set the fastest drawing speed
terrain_turtle.penup()

# Function to draw terrain
def draw_terrain():
    terrain_turtle.goto(-400, -20)  # Starting point
    terrain_turtle.pendown()

    # Draw the terrain
    for _ in range(160):
        terrain_turtle.color("green")
        terrain_turtle.forward(5)  # Move forward
        terrain_turtle.setheading(random.choice([0, 45, -45]))  # Turn randomly
        terrain_turtle.forward(random.randint(1, 10))  # Move up or down randomly

# Call the function to draw terrain
draw_terrain()

# Hide the turtle
terrain_turtle.hideturtle()

# Keep the window open
screen.mainloop()
