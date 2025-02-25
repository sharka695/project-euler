# dynamic programming:
# a 1 * 1 lattice has two routes from the top left:
# right, down
# down, right
# recursively, each other location for any lattice
# has a number of routes equal to the sum of the number of routes
# for the point to the right and the number of routes
# for the point to the left

def latticePaths(a, b):
    routes = [[1] * (b + 1) for i in range(a + 1)]
    for i in range(a - 1, -1, -1):
        for j in range(b - 1, -1, -1):
            routes[i][j] = routes[i + 1][j] + routes[i][j + 1]
    print(routes)
    return routes[0][0]

latticePaths(20, 20) # 137_846_528_820
