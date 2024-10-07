import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(order, size=300):
    t = turtle.Turtle()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window = turtle.Screen()
    window.bgcolor("white")

    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    koch_snowflake(t, order, size)

    window.mainloop()

# Виклик функції
koch_snowflake(3)
