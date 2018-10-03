
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

# OK... Now let's only run this if we're being called
# from OS
if __name__ == "__main__":
    # Variables (yay!)
    x1 = 2; y1 = 6
    x2 = 9; y2 = 4
    iterations = 100000
    
    # Show a nice display for user
    print("= Function arguments ======")
    print(" Point 1:    ({}, {})".format(x1, y1))
    print(" Point 2:    ({}, {})".format(x2, y2))
    print(" Iterations: {}".format(iterations))
    print()
    
    # Calculate results
    print("= Calculating =============")
    print()
    
    # Define the function parameters
    func_param = (x1, y1, x2, y2)
    
    # Time the different functions
    timing_ymxc = shared.time_function(gradient_function, func_param, iterations)  
    timing_bres = shared.time_function(bresenham_line_algo, func_param, iterations)       

    # Display gradient results
    shared.time_print("Gradient Function", timing_ymxc)
    print()
    shared.time_print("Bresenham Line Algo", timing_bres)
        
