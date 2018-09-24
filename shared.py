"""Shared componenets"""

iterations = 10

def print_array(array):
    """A nice printer for arrays"""
    for i in range(len(array)):
        print("{}, {}".format(i, array[i]))

def plot_create(width, height):
    """Creates a plottable array"""
    return [[False for x in range(width)] for y in range(height)]

def plot_render(array):
    """Render the plot"""
    for y in array:
        for x in y:
            print('*' if x else ' ')

def array_mean(array):
    """Calcualte the mean of the array"""

    # Add all the elements
    total = 0
    for el in array:
        total += el
    
    # Divide by number of elements
    return total / len(array)
