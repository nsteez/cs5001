from actor import Actor
from channel import Channel
from show import Show

def shows_starring(actor, channels):
    a_shows = []
    for available_channels in channels:
        a_shows += available_channels.get_shows_by_actor(actor)
    return a_shows

def function_a(channels, show_name):
    for channel in channels:
        for show in channel.broadcast_collection:
            #if show.title == show_name:
            for person in show.cast_members:
                print(person.firstname)


def main():
    actor1 = Actor("Anna", "Pen", 1)
    actor2 = Actor("Bailey", "Books", 3)
    actor3 = Actor("Netti", "Jones", 1)

    show1 = Show("Monday Show", [actor1, actor2], "Monday")
    show2 = Show("Wednesday Show", [actor3, actor2], "Wednesday")
    show3 = Show("Saturday Night Live", [actor2], "Saturday")

    channel1 = Channel("DEF", 42, [show3, show2])
    channel2 = Channel("XYZ", 32, [show2])
    channel3 = Channel("MNO", 56, [show3, show1])

    channels = [channel3, channel1, channel3]

    function_a(channels, "Saturday Night Live")


    list_shows = (shows_starring(actor1, channels))
    for show in list_shows:
       print(show.title)

    list_shows = (shows_starring(actor2, channels))
    for show in list_shows:
        print(show.title)

if __name__ == "__main__":
    main()
