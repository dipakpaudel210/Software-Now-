#!/usr/bin/env python3
# HIT137 Assignment 2 – Question 3
# Recursive inward-indented polygon pattern using turtle

import turtle

def draw_inward_edge(length, level):
    """Draw one edge with inward dents (recursively)."""
    if level == 0:
        turtle.forward(length)
        return

    part = length / 3
    # First segment
    draw_inward_edge(part, level - 1)

    # Draw the inward "triangle" shape
    turtle.right(60)
    draw_inward_edge(part, level - 1)
    turtle.left(120)
    draw_inward_edge(part, level - 1)
    turtle.right(60)

    # Last segment
    draw_inward_edge(part, level - 1)

def draw_polygon(sides, length, level):
    turn_angle = 360 / sides
    for _ in range(sides):
        draw_inward_edge(length, level)
        turtle.left(turn_angle)

def main():
    print("Drawing recursive polygon...")

    sides = int(input("Number of sides: "))
    length = float(input("Side length (pixels): "))
    level = int(input("Recursion depth: "))

    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-length/2, 0)  # start roughly centered
    turtle.pendown()

    draw_polygon(sides, length, level)

    print("Done. Close the window to exit.")
    turtle.done()

if __name__ == "__main__":
    main()
