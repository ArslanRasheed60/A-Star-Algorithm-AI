import math
import state

HURDLE = 2
START_STATE = 1
ALREADY_EXPLORED = 11


# exact heuristic using euclidean distance
def calculateHeuristic(currentState: state, goalState: state):
    return float(
        math.sqrt(((goalState.x - currentState.x) ** 2) + ((goalState.y - currentState.y) ** 2)))


# get minimum cost item from the list
def calculateMinCostIndex(listItems):
    index = 0
    minValue = listItems[0].calculateTotalCost()

    for i in range(0, len(listItems)):
        if minValue > (listItems[i].calculateTotalCost()):
            minValue = listItems[i].calculateTotalCost()
            index = i

    return index


# explore top
def explore_top(presentState: state, grid):
    if presentState.y - 1 < 0:
        return None
    if (grid[presentState.y - 1][presentState.x] != HURDLE and
            grid[presentState.y - 1][presentState.x] != START_STATE):
        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x and
                    presentState.parent.y == presentState.y - 1):
                return None

        newState = state.StateClass()
        newState.x = presentState.x
        newState.y = presentState.y - 1
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True

        return newState
    return None


# explore right
def explore_right(presentState: state, grid):
    if presentState.x + 1 >= len(grid[0]):
        return None
    if (grid[presentState.y][presentState.x + 1] != HURDLE and
            grid[presentState.y][presentState.x + 1] != START_STATE):

        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x + 1 and
                    presentState.parent.y == presentState.y):
                return None

        newState = state.StateClass()
        newState.x = presentState.x + 1
        newState.y = presentState.y
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True
        return newState
    return None


# explore bottom
def explore_bottom(presentState: state, grid):
    if presentState.y + 1 >= len(grid):
        return None
    if (grid[presentState.y + 1][presentState.x] != HURDLE and
            grid[presentState.y + 1][presentState.x] != START_STATE):

        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x and
                    presentState.parent.y == presentState.y + 1):
                return None

        newState = state.StateClass()
        newState.x = presentState.x
        newState.y = presentState.y + 1
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True

        return newState
    return None


# explore left
def explore_left(presentState: state, grid):
    if presentState.x - 1 < 0:
        return None
    if (grid[presentState.y][presentState.x - 1] != HURDLE and
            grid[presentState.y][presentState.x - 1] != START_STATE):

        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x - 1 and
                    presentState.parent.y == presentState.y):
                return None

        newState = state.StateClass()
        newState.x = presentState.x - 1
        newState.y = presentState.y
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True

        return newState
    return None


# explore top-right
def explore_topRight(presentState: state, grid):
    if presentState.y - 1 < 0 or presentState.x + 1 >= len(grid[0]):
        return None
    if (grid[presentState.y - 1][presentState.x + 1] != HURDLE and
            grid[presentState.y - 1][presentState.x + 1] != START_STATE):

        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x + 1 and
                    presentState.parent.y == presentState.y - 1):
                return None

        newState = state.StateClass()
        newState.x = presentState.x + 1
        newState.y = presentState.y - 1
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True

        return newState
    return None


# explore bottom-right
def explore_bottomRight(presentState: state, grid):
    if presentState.y + 1 >= len(grid) or presentState.x + 1 >= len(grid[0]):
        return None
    if (grid[presentState.y + 1][presentState.x + 1] != HURDLE and
            grid[presentState.y + 1][presentState.x + 1] != START_STATE):

        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x + 1 and
                    presentState.parent.y == presentState.y + 1):
                return None

        newState = state.StateClass()
        newState.x = presentState.x + 1
        newState.y = presentState.y + 1
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True

        return newState
    return None


# explore top-left
def explore_topLeft(presentState: state, grid):
    if presentState.y - 1 < 0 or presentState.x - 1 < 0:
        return None
    if (grid[presentState.y - 1][presentState.x - 1] != HURDLE and
            grid[presentState.y - 1][presentState.x - 1] != START_STATE):

        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x - 1 and
                    presentState.parent.y == presentState.y - 1):
                return None

        newState = state.StateClass()
        newState.x = presentState.x - 1
        newState.y = presentState.y - 1
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True

        return newState
    return None


# explore bottom-left
def explore_bottomLeft(presentState: state, grid):
    if presentState.y + 1 >= len(grid) or presentState.x - 1 < 0:
        return None
    if (grid[presentState.y + 1][presentState.x - 1] != HURDLE and
            grid[presentState.y + 1][presentState.x - 1] != START_STATE):

        # prevent cycles
        if presentState.parent is not None:
            if (presentState.parent.x == presentState.x - 1 and
                    presentState.parent.y == presentState.y + 1):
                return None

        newState = state.StateClass()
        newState.x = presentState.x - 1
        newState.y = presentState.y + 1
        newState.parent = presentState
        newState.cost = presentState.cost + 1

        # if grid[newState.y][newState.x] == 0:
        #     grid[newState.y][newState.x] = ALREADY_EXPLORED
        #     newState.isVisited = False
        # elif ALREADY_EXPLORED <= grid[newState.y][newState.x] <= MAXEXPLORED:
        #     grid[newState.y][newState.x] += 1
        #     newState.isVisited = False
        # else:
        #     newState.isVisited = True

        if grid[newState.y][newState.x] != ALREADY_EXPLORED:
            grid[newState.y][newState.x] = ALREADY_EXPLORED
            newState.isVisited = False
        else:
            newState.isVisited = True

        return newState
    return None
