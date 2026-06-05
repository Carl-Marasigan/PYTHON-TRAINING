import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def volume_of_cylinder(radius, height):
    return area_of_circle(radius) * height

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
