class Module(object):

    def __init__(self, name):
        self.name       = name
        self.parent     = None
        self.submodules = []
        self.wires      = []

    def add_submodule(self, new_submodule):
        new_submodule.set_parent(self)
        self.submodules.append(new_submodule)

    def add_submodules(self, new_submodules):
        for module in new_submodules:
            module.set_parent(self)

        self.submodules.extend(new_submodules)

    def add_wire(self, new_wire):
        self.wires.append(new_wire)

    def add_wires(self, new_wires):
        self.wires.extend(new_wires)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_fullname(self):
        parent_fullname = parent.get_fullname() if parent else ""
        return "%s/%s" % (parent_fullname, self.get_name())

    def tree(self, depth = 1, include_wires = True):
        temp_tree = "%s%s%s\n"%(" "*4*(depth-1), "|===", self.name)
        if include_wires:
            for wire in self.wires:
                temp_tree += "%s%s%s\n"%(" "*4*(depth), "|---", wire.get_name())
        for submodule in self.submodules:
            temp_tree += submodule.tree(depth+1)
        return temp_tree

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent
