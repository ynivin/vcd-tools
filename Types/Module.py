class Module(object):

    def __init__(self, name):
        self.name       = name
        self.parent     = None
        self.submodules = {}
        self.wires      = {}

    def add_submodule(self, new_submodule):
        new_submodule.set_parent(self)
        self.submodules[new_submodule.get_name()] = new_submodule

    def add_submodules(self, new_submodules):
        for module in new_submodules:
            module.set_parent(self)
            self.submodules[module.get_name()] = module

    def add_wire(self, new_wire):
        self.wires[new_wire.get_name()] = new_wire

    def add_wires(self, new_wires):
        self.wires.update({wire.get_name(): wire for wire in new_wires})

    def get_name(self):
        return self.name

    def get_fullname(self):
        parent_fullname = self.parent.get_fullname() if self.parent else ""
        return "%s/%s" % (parent_fullname, self.get_name())

    def tree(self, depth = 1, include_wires = True):
        temp_tree = "%s%s%s\n"%(" "*4*(depth-1), "|===", self.get_name())
        if include_wires:
            for wire in self.wires.values():
                temp_tree += "%s%s%s\n"%(" "*4*(depth), "|---", wire.get_name())
        for submodule in self.submodules.values():
            temp_tree += submodule.tree(depth+1)
        return temp_tree

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent
