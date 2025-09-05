import turtle

def draw_edge(length, depth):
    """Recursive function to draw a fractal edge."""
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.left(60)
        draw_edge(length, depth - 1)
        turtle.right(120)
        draw_edge(length, depth - 1)
        turtle.left(60)
        draw_edge(length, depth - 1)

def draw_polygon(sides, length, depth):
    """Draws the polygon with fractal edges."""
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(360 / sides)

# Main program
if __name__ == "__main__":
    turtle.speed(0)  # Fastest drawing speed
    turtle.hideturtle()

    # User input
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    draw_polygon(sides, length, depth)

    turtle.done()
