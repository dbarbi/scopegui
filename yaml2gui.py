#! /usr/bin/env python3

from tkinter import *
from buttonfunctions import *
from file_reader import *

from tkinter_interface import *
#from web_interface import *



class window:
    def __init__(self, config, name):
        self.config = config[name]
        self.name = name

        if not "globals" in self.config:
            self.config["globals"] = {}

        self.needs = needs()
        self.canvas = None

        self.things = {}

        self.buttons = {}
        self.labels = {}
        self.circles = {}
        self.lines = {}

        self.default_canvas_size()

        check(self.needs.all("window"), self.config)

        self.window = Tk()

        self.draw_all()





    def mainloop(self):
        self.window.mainloop()



    def default_canvas_size(self):
        if not "canvas" in self.config:
            # default canvas size is whole window
            self.config["canvas"]["x"] = self.config["x"]
            self.config["canvas"]["y"] = self.config["y"]
            self.config["canvas"]["width"] = self.config["width"]
            self.config["canvas"]["height"] = self.config["height"]



    def draw_all(self):
        self.interpret_window()

        for thing in known_things:
            self.add_all(thing)


    def wrap_around(self, function): 
        # poorly written, better look for changes and just redraw those
        self.config = globals()[function](self.config)
        self.draw_all()


    def add_all(self, thing):
        if thing in self.config:
            if thing in unique_things:
                self.add(thing, self.config[thing], thing)
            else:
                for thisthing in self.config[thing]:
                    self.add(thing, self.config[thing][thisthing], thisthing)

    def add(self, thing, config, thisthing):
        check(self.needs.all(thing), config)
        getattr(self, "erase_" + thing)(thisthing, config)
        getattr(self, "draw_" + thing)(thisthing, config)




# ################################################################
#                     Window stuff
# ################################################################

    def interpret_window(self):
        self.size_x = self.config["width"]
        self.size_y = self.config["height"]
        self.geometry = str(self.size_x) + "x" + str(self.size_y)
        self.window.geometry(self.geometry)

        self.title = self.config["title"]
        self.window.title(self.title)











# ################################################################
#                     Canvas stuff
# ################################################################

    def draw_canvas(self, canvas, config):
        check(self.needs.all("canvas"), self.config["canvas"])
        self.canvas = Canvas(
                self.window
                )
        self.canvas.config(
                width = self.config["canvas"]["width"],
                height = self.config["canvas"]["height"],
                )
        self.canvas.place(
                x = self.config["canvas"]["x"],
                y = self.config["canvas"]["y"],
                width = self.config["canvas"]["width"],
                height = self.config["canvas"]["height"],
                )


    def erase_canvas(self, canvas, config):
        if self.canvas:
            del self.canvas
            self.canvas = None



# ################################################################
#                     Lines stuff
# ################################################################


    def erase_line(self, line, config):
        if line in self.lines:
            self.canvas.delete(self.lines[line])
            del self.lines[line]



    def draw_line(self, line, config):
        self.lines[line] = self.canvas.create_line(
                config["from_x"],
                config["from_y"],
                config["to_x"],
                config["to_y"],
                )


# ################################################################
#                     Circle stuff
# ################################################################


    def erase_circle(self, circle, config):
        if circle in self.circles:
            self.canvas.delete(self.circles[circle])
            del self.circles[circle]


    def draw_circle(self, circle, config):
        self.circles[circle] = self.canvas.create_oval(
                config["x"] - config["radius"],
                config["y"] - config["radius"],
                config["x"] + config["radius"],
                config["y"] + config["radius"],
                )
        self.circles[circle] = self.canvas.create_oval(
                config["x"] - config["radius"],
                config["y"] - config["radius"],
                config["x"] + config["radius"],
                config["y"] + config["radius"],
                )


# ################################################################
#                     Button stuff
# ################################################################


    def draw_button(self, button, config):
        check(self.needs.all("button"), config)
        self.buttons[button] = Button(
                self.window, 
                command = lambda: self.wrap_around(config["command"])
                )
        self.buttons[button].config(
                text = config["text"]
                )
        if "x" in config:
            check(["y", "width", "height"], config)
            self.buttons[button].place(
                    x = config["x"],
                    y = config["y"],
                    width = config["width"],
                    height = config["height"],
                    )
        else:
            self.buttons[button].pack()


    def erase_button(self, button, config):
        if button in self.buttons:
            del self.buttons[button]



# ################################################################
#                     Label stuff
# ################################################################



    def draw_label(self, label, config):
        check(self.needs.all("label"), config)
        self.labels[label] = Label(
                self.window, 
                text=config["text"],
                )
        self.labels[label].config(
                text=config["text"],
                )
        if "x" in config:
            check(["y", "width", "height"], config)
            self.labels[label].place(
                    x = config["x"],
                    y = config["y"],
                    width = config["width"],
                    height = config["height"],
                    )
        else:
            self.labels[label].pack()


    def erase_label(self, label, config):
        if label in self.labels:
            del self.labels[label]
















