class Module:

    def __init__(self, name, submodules = [], wires = []):
        self.name       = name
        self.submodules = submodules
        self.wires      = wires

    def add_submodule(self, new_submodule):
        submodules.append(new_submodule)

    def add_submodules(self, new_submodules):
        submodules.extend(new_submodules)

    def add_wire(self, new_wire):
        wires.append(new_wire)

    def add_wires(self, new_wires):
        wires.extend(new_wires)
