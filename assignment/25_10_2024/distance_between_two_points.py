import math

RADIUS_OF_EARTH = 6371.01
point_x1 = float(input("Input the latitude of coordinate 1: "))
point_y1 = float(input("Input the longititude of coordinate 1: "))
point_x2 = float(input("Input the latitude of coordinate 2: "))
point_y2 = float(input("Input the longititude of coordinate 2: "))

distance = RADIUS_OF_EARTH * math.acos(math.sin(point_x1) * math.sin(point_x2) + math.cos(point_x1) * math.cos(point_x2) * math.cos(point_y1 - point_y2))

printf(f"The distance between those points is: {distance}km\n")

