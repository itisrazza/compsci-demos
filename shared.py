"""Shared componenets"""

import time

iterations = 10

def print_array(array):
    """A nice printer for arrays"""
    for i in range(len(array)):
        print("{}, {}".format(i, array[i]))

def plot_create(width, height):
    """Creates a plottable array"""
    return [[False for x in range(width)] for y in range(height)]

def plot_render(plot):
    """Render the plot"""
    for y in plot:
        for x in y:
            print('*' if x else ' ', end="")
        print()

def plot_points(plot, points):
    """Plots the specified points on the plot"""
    for point in points:
        plot[point[0]][point[1]] = True
    return plot

def array_mean(array):
    """Calcualte the mean of the array"""

    # Add all the elements
    total = 0
    for el in array:
        total += el
    
    # Divide by number of elements
    return total / len(array)

def time_function(function, func_args=(), iterations=iterations, timing_func=time.time):
    """Times a function and returns timing results"""
    
    # Lists for times and results
    results = []
    times = []
    
    # Start timing
    time_start = timing_func()
    
    # Go through the iterations, appending each lap
    for i in range(iterations):
        function(*func_args)
        times.append(timing_func())
        
    # Take not of the last timing
    time_finish = timing_func()

    # Calculate the last time
    time_span = time_finish - time_start
    
    # Prepare result
    result = {}
    result["time"] = {}
    result["time"]["span"] = time_span
    result["time"]["start"] = time_start
    result["time"]["finish"] = time_finish
    result["time"]["laps"] = times
    result["func"] = {}
    result["func"]["results"] = results
    result["func"]["args"] = func_args
    result["iterations"] = iterations
    #result[""] =  
    
    # Give it to the world (or just the called)
    return result

def time_print(title, timings):
    print("= {} =".format(title))
    print(" Time Span:   {}".format(timings["time"]["span"]))
    print(" Iterations:  {}".format(timings["iterations"]))
    print(" Average lap: {}".format(timings["time"]["span"] / timings["iterations"]))
    return





