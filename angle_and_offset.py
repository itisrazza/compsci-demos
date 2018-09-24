
import sys
import math

x1 = input("Point 1 X: ")
y1 = input("        Y: ")
x2 = input("Point 2 X: ")
y2 = input("        Y: ")

try:
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
except ValueError as ex:
    print("Value Error")
    sys.exit(1)

delta_x = abs(x2 - x1)
delta_y = abs(y2 - y1)

angle = math.atan(delta_y / delta_x)

print("Angle (radians): {}".format(angle))
print("Angle (degrees): {}°".format(math.degrees(angle)))

