class Wire:
    """ Represents wire, which is a single node with variable width """

    def __init__(self, name, width, dumps):
        self.name   = name
        self.width  = width
        self.dumps  = dumps

    def get_name(self):
        return self.name
