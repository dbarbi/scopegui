from file_reader import *
from math import pi, sin, cos

def add_model(config):
    config["globals"]["number_of_models"] += 1
    bubble_radius = config["globals"]["bubble_radius"]

    if not "circle" in config:
        config["circle"] = {}

    total_number = config["globals"]["number_of_models"]
    this_number = 1
    for circle in config["circle"]:
        x, y = get_circle_coordinates(config, total_number, this_number)
        config["circle"][circle]["x"] = x
        config["circle"][circle]["y"] = y
        config["circle"][circle]["radius"] = bubble_radius
        this_number += 1

    circle = total_number
    x, y = get_circle_coordinates(config, total_number, this_number)
    config["circle"][circle] = {}
    config["circle"][circle]["x"] = x
    config["circle"][circle]["y"] = y
    config["circle"][circle]["radius"] = bubble_radius

    config["label"]["number"]["text"] = str(config["globals"]["number_of_models"]) + " models"

    return config


def reset_window(config):
    reset_config = read_config_file("gui.yaml")
    return reset_config["main_window"]


def get_circle_coordinates(config, total_number, this_number):

    center_x = config["globals"]["center_x"]
    center_y = config["globals"]["center_y"]
    organigram_radius = config["globals"]["organigram_radius"]

    if total_number == 1:
        return center_x, center_y
    
    if this_number == 1:
        return center_x, center_y - organigram_radius

    angle = 2 * pi / total_number * ( this_number - 1) 

    new_x = center_x + sin(angle) * organigram_radius
    new_y = center_y - cos(angle) * organigram_radius

    return new_x, new_y


