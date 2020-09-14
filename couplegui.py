#! /usr/bin/env python3

from yaml2gui import *
from file_reader import *

filename = "gui.yaml"

config = read_config_file(filename)
fenster = window(config, "main_window")

fenster.mainloop()
