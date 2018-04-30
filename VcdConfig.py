from Types.Dumps import Dumps


class VcdConfig(object):

    def __init__(self):
        self.dumps_ids = {}

    def get_dumps_by_id(self, id):
        if id not in self.dumps_ids:
            self.dumps_ids[id] = Dumps()
        return self.dumps_ids[id]


class Vcd(object):

    def __init__(self, top_module, vcd_config):
        self.top_module = top_module
        self.vcd_config = vcd_config

    def get_top_module(self):
        return self.top_module

    def set_top_module(self, top_module):
        self.top_module = top_module

    def get_vcd_config(self):
        return self.vcd_config

    def set_vcd_config(self, vcd_config):
        self.vcd_config = vcd_config
