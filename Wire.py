class Wire:
    """ Represents wire, which is a single node with variable width """

    def __init__(self, width, name, dumps):
        self.width  = width
        self.name   = name
        self.dumps  = dumps
