
import time
import math
import shared

def gradient_function(x1, y1, x2, y2):
    """The classic `y = mx + c` equation we all know and love."""
    
    points = []
    
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1

    for x in range(x1 + 1, x2):
        points.append((x, round(m * x + c)))

    return points

def bresenham_line_algo(x1, y1, x2, y2):
    """The Bresenham Line Algorithm"""

    points = []

    A = 2 * abs(y2 - y1)
    B = A - 2 * (x2 - x1)
    P = A - (x2 - x1)

    y = y1

    for x in range(x1 + 1, x2):
        P += A if P < 0 else B
        y += 0 if P < 0 else 1

    return points

# Variables (yay!)
x1 = 2; y1 = 6
x2 = 9; y2 = 4
iterations = 1000000

# Show a nice display for user
print("= Function arguments ======")
print(" Point 1:    ({}, {})".format(x1, y1))
print(" Point 2:    ({}, {})".format(x2, y2))
print(" Iterations: {}".format(iterations))
print()

# Calculate results
print("= Calculating =============")
print()

# Use a consistent timing function
timing_function = time.time

# Gradient function
times = []  # Laps
time_start = timing_function()
for i in range(iterations):
    gradient_function(x1, y1, x2, y2)
    times.append(timing_function())
time_finish = timing_function()
time_span = time_finish - time_start

# Display gradient results
print("= Gradient Function =======")
print(" Time span:          {}".format(time_span))
print(" Iterations:         {}".format(iterations))
print(" Average lap (t/l):  {}".format(time_span / iterations))
print()

# Bresenham's
times = []  # Laps
time_start = timing_function()
for i in range(iterations):
    bresenham_line_algo(x1, y1, x2, y2)
    times.append(timing_function())
time_finish = timing_function()
time_span = time_finish - time_start

# Display gradient results
print("= Gradient Function =======")
print(" Time span:          {}".format(time_span))
print(" Iterations:         {}".format(iterations))
print(" Average lap (t/l):  {}".format(time_span / iterations))
print()
