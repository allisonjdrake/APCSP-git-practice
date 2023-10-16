#DIJKSTRA Algo:  (the weird chart thingies)
#     finds the shortest path between one point and every other point
#     need to know 
# Directional: 
#     has arrows
#     (some don't, they are considered as not having direction)
# Weighted:
#     has numbers
#     (some don't, they are considered unweighted)

# Uses:
#     Anything you want, but best for problems searching for optimal paths
#         Ex: rock paper scissors
#         Ex: traveling salesman


##BREADTH vs. DEPTH
#Breadth: search based on distance - search every level (one step away --> search two steps away --> search three, etc.)
    #level by level
    #FIFO: First in, first out

#Depth: go down rabbit hole - find first thing connected to the first node, from there go to the next, go down
    #until you can't go anymore --> start from the beginning and do the same
    #branch by branch
    #LIFO: Last in, first out

