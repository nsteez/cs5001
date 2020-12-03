#from actor import Actor


class Show:
    def __init__(self, title, cast_members):
        self.title = title
        self.cast_members = cast_members

    def cast_contains(self, Actor):
        return True if Actor in self.cast_members else False
