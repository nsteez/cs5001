from actor import Actor
from channel import Channel
from show import Show


def main():

    actor1 = Actor("Anna", "Pen", 1)
    actor2 = Actor("Bailey", "Books", 3)
    actor3 = Actor("Netti", "Jones", 1)

    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Wednesday Show"[actor3, actor2])
    show3 = Show("Saturday Night Live" [actor2])

    channel1 = Channel("DEF", 42, [show1])
    channel2 = Channel("XYZ", 32, [show2])
    channel3 = Channel("MNO", 56, [show3, show1])

    channel = [channel1, channel2, channel3]

if __name__ == "__main__":
    main()
