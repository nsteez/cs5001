"""
Netti Welsh
CS5001 - Fall202
Lab 9 - Turtle
"""
import turtle

def main():
    DEGREE_ROTATION = 144
    MAX_SEGMENT_SIZE = 200
    SEGMENT_INCREASE = 10
    LAST_LINE = 4

    turt = turtle.Turtle()
    colors = ["red", "yellow", "orange", "pink", "purple"]
    segment = SEGMENT_INCREASE
    index = 0
    turt.pensize(4)
    while segment < MAX_SEGMENT_SIZE:
        turt.color(colors[index])
        turt.forward(segment)
        turt.right(DEGREE_ROTATION)
        if(index == LAST_LINE):
            index = 0
        else:
            index+=1
        segment+=SEGMENT_INCREASE

    turtle.done()


if __name__  == "__main__":
    main()