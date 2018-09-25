
graph = [[False for x in range(80)] for y in range(25)]

def print_graph():
    for y in graph:
        for x in y:
            print('*' if x else ' ', end='')
        print()

def print_array(array):
    for i in range(len(array)):
        print("({}, {})".format(i, array[i]))

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
            
print("Array data")
print_array(bresenham_midpoint(0, 0, 10))
    
print("Rendering")
print_array(bresenham_midpoint(40, 12, 10))
