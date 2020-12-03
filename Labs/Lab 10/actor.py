class Actor:
    def __init__(self, firstname, lastname, actors_shows):
        self.firstname = firstname
        self.lastname = lastname
        self.actors_shows = actors_shows

    def __eq__(self, other):
        if self.firstname == other.firstname and\
        self.lastname == other.lastname:
            return True
        return False