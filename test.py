import Parse
c=Parse.parse_vcd("example.vcd")
print(c.get_top_module().tree())
