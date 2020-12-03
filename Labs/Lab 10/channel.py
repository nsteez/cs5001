class Channel:
    def __init__(self, name, number, broadcast_collection):
        self.name = name
        self.number = number
        self.broadcast_collection = broadcast_collection

    def get_shows_by_actor(self, Actor):
        showlist = []
        for sh in self.broadcast_collection:
            if sh.cast_contains(Actor):
                showlist.append(sh)
        return showlist

    def shows(self):
        for show in self.broadcast_collection:
            print(show.day_broadcast)
