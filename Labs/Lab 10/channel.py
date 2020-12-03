#from actor import Actor

class Channel:
    def __init__(self, name, number, broadcast_collection):
        self.name = name
        self.number = number
        self.broadcast_collection = broadcast_collection
    def get_shows_by_actor(self, Actor):
        showlist = []
        for sh in broadcast_collection:
            if sh.cast_contains(Actor):
                showlist.append(sh)
        return showlist
