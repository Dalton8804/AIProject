from Node import Node

root = Node(value="rrrbggg", cost=0, level=0)
tree = {}
valueTree = {}

levelCount = {0: 1}
needToAdd = []


def createLevel(node):
    tree[node] = node.getChildren()
    count = 0
    for node in tree[node]:
        count += 1
        needToAdd.append(node)
    if node.level in levelCount:
        levelCount[node.level] += count
    else:
        levelCount[node.level] = count


createLevel(root)

while len(needToAdd) > 0:
    createLevel(needToAdd.pop(0))


def pathToGoal(node, arr):
    if node.parent is not None:
        arr = pathToGoal(node.parent, arr)
    arr += " -> " + node.value
    return arr


# Start BFS
'''
visited = []
queue = []


def bfs(visited, tree, node):
    visited.append(node)
    queue.append(node)

    while queue:
        curr = queue.pop(0)
        if curr.isGoal():
            print("\nLevel Found: " + str(curr.level) + " Total Cost: " + str(curr.totalCost) + " State: " + curr.value)
            print("Path from root: " + str(pathToGoal(curr, "")), end="\n\n")
        for neighbor in tree[curr]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


bfs(visited, tree, root)
'''


# Start A* Search

def h(node):
    # count the number of r's on the left side of the leftmost g
    n = node.value
    numOfRMisplaced = 3
    rCount = 0
    gCount = 0
    for x in n:
        if x == 'r':
            rCount += 1
            if gCount == 3:
                numOfRMisplaced -= 1
        elif x == 'g':
            gCount += 1
        else:
            pass
    return node.cost + numOfRMisplaced


def aStarSearch(node):
    # Initialize lists, step 1
    OPEN = [(node, h(node))]
    CLOSED = []

    # if OPEN is empty return failure, step 2
    while len(OPEN) > 0:

        # choose the lowest h(n) of successors, step 3
        lowestChoice = OPEN[0]
        for x in OPEN:
            if x[1] < lowestChoice[1]:
                lowestChoice = x
        if lowestChoice[0].isGoal():
            print("Shortest Path: "+str(pathToGoal(lowestChoice[0], "")))
            return lowestChoice[0].value + " SUCCESS"

        # Expand the lowest choice node and add each successor to the open list and close that node, step 4
        CLOSED.append(lowestChoice)
        OPEN.remove(lowestChoice)
        for n in tree[lowestChoice[0]]:
            if n not in OPEN and n not in CLOSED:
                OPEN.append((n, h(n)))

        print(lowestChoice[0].value)
    # return to step 2 if list not empty and goal not found
    return 'FAILURE'


print(aStarSearch(root))
