
import time
import math
import shared

def trigonometry(x, y, r):
    points = []
    
    # Assume 360deg data points
    for angle in range(360):
        # Convert angle to radians
        angle_rad = math.radians(angle)
        # So some trig magic on them
        points.append((x + (r * math.cos(angle_rad)), y + (r * math.sin(angle_rad))))    

    # Return the points to caller
    return points

def pythagoras(x, y, r):
    points = []
    
    # I have no idea on making this more efficient.
    # This is just a port to Python of some code from earlier this year
    
    # Just get x for every horizontal line
    for i in range(x - r, x + r):
        points.append((i, y + math.sqrt(abs(math.pow(r, 2) - math.pow(i, 2)))))
        # print(math.sqrt(abs(math.pow(r, 2) - math.pow(i, 2))))
        # A reflection would also need to be drawn, but later
    
    return points

def bresenham_midpoint(x, y, r):
    points = []
    
    E = -r
    X = r
    Y = 0
    
    while Y <= X:
        points.append((x + X, y + Y))
        E += 2 * Y + 1
        Y += 1
        if E <= 0:
            E -= 2 * X - 1
            X -= 1
            
    return points
    
def bresenham_circle(x, y, r):
    points = []
    
    # Using Bresenham's algo to get the circle
    algo_points = bresenham_midpoint(0, 0, r)
    
    # Offset the original points
    for point in algo_points:

        # Redefine variables for reasons
        x_ = point[0]
        y_ = point[1]
        
        # Top half
        points.append(( x + x_, y + y_)) #    0 deg ~   45 deg
        points.append(( x + y_, y - x_)) #   45 deg ~   90 deg
        points.append(( x + y_, y + x_)) #   90 deg ~  135 deg
        points.append(( x - x_, y + y_)) #  135 deg ~  180 deg
        
        # Bottom half
        points.append(( x - x_, y - y_)) #  180 deg ~ -135 deg
        points.append(( x - y_, y + x_)) # -135 deg ~  -90 deg
        points.append(( x - y_, y - x_)) #  -90 deg ~  -45 deg
        points.append(( x + x_, y - y_)) #  -45 deg ~    0 deg
        
    # Return
    return points

# If this is the program to be called,
# do the tests
if __name__ == "__main__":
    # Variables (yay!)
    x = 5; y = 5; r = 5
    iterations = 100000  
    
    # Show the settings to the user
    print("= Function arguments =")
    print(" Center:     ({}, {})".format(x, y))
    print(" Radius:     {}".format(r))
    print(" Iterations: {}".format(iterations))
    print()
    
    # Calculate results
    print("= Calculating =")
    print()
    
    # Define the function parameters
    func_param = (x, y, r)
    
    # Time the functions
    timing_pyta = shared.time_function(pythagoras, func_param, iterations)
    timing_trig = shared.time_function(trigonometry, func_param, iterations)
    timing_bres = shared.time_function(bresenham_circle, func_param, iterations)
    
    # Display results
    shared.time_print("Pythagoras' Theorem", timing_pyta)
    print()
    shared.time_print("Trigonometry", timing_trig)
    print()
    shared.time_print("Bresenham's Midpoint Algo (8x)", timing_bres)
    
    # That's it
    
