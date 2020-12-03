class Show:
    def __init__(self, title, cast_members, broadcast):
        self.title = title
        self.cast_members = cast_members
        self.day_broadcast = broadcast

    def __str__(self):
        return "Show name: " + self.title + " shown on " + self.day_broadcast

    def get_cast_members(self):
        return self.cast_members

    def get_title(self):
        return self.title

    def cast_contains(self, Actor):
        return True if Actor in self.cast_members else False
