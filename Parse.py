from Types.Module import Module
from Types.Wire import Wire
from VcdConfig import VcdConfig
from VcdConfig import Vcd


def parse_vcd(filename):
    vcd_config = VcdConfig()
    with open(filename, "r") as vcd_file:
        vcd_lines = vcd_file.readlines()

    top_module = Module(name = "root")
    current_module = top_module

    dumpvars_section = False
    lines_iter = iter(vcd_lines)
    while not dumpvars_section:
        line = lines_iter.next()
        line_words = line.split()
        if not line_words:
            pass
        elif line_words[0] == "$scope":
            new_module = Module(name = line_words[2])
            current_module.add_submodule(new_module)
            current_module = new_module
        elif line_words[0] == "$upscope":
            current_module = current_module.get_parent()
        elif line_words[0] == "$var":
            wire_name = line_words[4]
            wire_width = line_words[2]
            wire_dumps_id = line_words[3]
            current_module.add_wire(Wire(wire_name,
                                            wire_width,
                                            vcd_config.get_dumps_by_id(wire_dumps_id)))
        elif line_words[0] == "$dumpvars":
            dumpvars_section = True

    time = -1
    for line in lines_iter:
        line_words = line.split()
        if not line_words:
            pass
        elif line_words[0][0] in ['0', '1', 'x', 'X', 'z', 'Z']:
            vcd_config.get_dumps_by_id(line_words[0][1:]).add_dumps({time: line_words[0][0]})
        elif line_words[0][0] in ['b', 'B']:
            vcd_config.get_dumps_by_id(line_words[1]).add_dumps({time: line_words[0][1:]})
        elif line_words[0][0] == '#':
            time = int(line_words[0][1:])

    return Vcd(top_module, vcd_config)
