# vcd-tools
Python library for creating, modifying and parsing VCD (Value change dump) files

### Current status
Basic modeling of dump file. `parce_vcd(filename)` function in Parse.py will parse the VCD file and return a Vcd object.

### TODO
- Project structure
  - [ ] Group the classes in files
  - [ ] Clean import statements
- Issues
  - [ ] submodules and wires should be stored in dict instead of list, with name as key
- Near future
  - [ ] write_vcd function from top_module & vcd_config
  - [ ] Compare functions