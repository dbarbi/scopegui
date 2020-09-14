#! /usr/bin/env python3

class needs:
    def __init__(self):
        self.config = read_config_file("needs.yaml")

    def all(self, elementtype, name = None):
        if name:
            needlist = [name]
        else:
            needlist = []
        for entry in self.config[elementtype]:
            if name:
                needlist += [ name + ":" + entry ]
            else:
               needlist += [ entry ]
        return needlist

def check(list_of_entries, config):
    if isinstance(list_of_entries, str):
        list_of_entries = [list_of_entries]
    for entry in list_of_entries:
        if ":" in entry:
            way_to_entry = entry.split(":")
        else:
            way_to_entry = [entry]
        thisconfig = config
        for step in way_to_entry:
            if not step in thisconfig:
                print(config)
                print(thisconfig)
                print("Entry " + str(way_to_entry) + " is missing in gui yaml file")
                sys.exit(-1)
            thisconfig = thisconfig[step]

def read_config_file(filename):
    # yaml-import config
    import yaml
    with open (filename) as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    #print(config)
    return config

