import state
import A_Star_methods


# import gridAp

def Algorithm(currentState: state, goalState: state, grid):
    # initializing open and closed list
    openList = []
    closedList = []

    openList.append(currentState)

    while len(openList) != 0:
        # print(1)
        index = A_Star_methods.calculateMinCostIndex(openList)
        presentState = openList.pop(index)

        print("y: ", presentState.y, "-x: ", presentState.x, grid[presentState.y][presentState.x])

        # if goal found return true
        if presentState.x == goalState.x and presentState.y == goalState.y:
            return presentState

        # explore top state
        topState = A_Star_methods.explore_top(presentState, grid)
        if topState is not None:
            topState.heuristic = A_Star_methods.calculateHeuristic(topState, goalState)
            if topState.isVisited is False:
                openList.append(topState)

        # explore right state
        rightState = A_Star_methods.explore_right(presentState, grid)
        if rightState is not None:
            rightState.heuristic = A_Star_methods.calculateHeuristic(rightState, goalState)
            if rightState.isVisited is False:
                openList.append(rightState)

        # explore bottom state
        bottomState = A_Star_methods.explore_bottom(presentState, grid)
        if bottomState is not None:
            bottomState.heuristic = A_Star_methods.calculateHeuristic(bottomState, goalState)
            if bottomState.isVisited is False:
                openList.append(bottomState)

        # explore left state
        leftState = A_Star_methods.explore_left(presentState, grid)
        if leftState is not None:
            leftState.heuristic = A_Star_methods.calculateHeuristic(leftState, goalState)
            if leftState.isVisited is False:
                openList.append(leftState)

        # explore top-right state
        topRightState = A_Star_methods.explore_topRight(presentState, grid)
        if topRightState is not None:
            topRightState.heuristic = A_Star_methods.calculateHeuristic(topRightState, goalState)
            if topRightState.isVisited is False:
                openList.append(topRightState)

        # explore bottom-right state
        bottomRightState = A_Star_methods.explore_bottomRight(presentState, grid)
        if bottomRightState is not None:
            bottomRightState.heuristic = A_Star_methods.calculateHeuristic(bottomRightState, goalState)
            if bottomRightState.isVisited is False:
                openList.append(bottomRightState)

        # explore top-left state
        topLeftState = A_Star_methods.explore_topLeft(presentState, grid)
        if topLeftState is not None:
            topLeftState.heuristic = A_Star_methods.calculateHeuristic(topLeftState, goalState)
            if topLeftState.isVisited is False:
                openList.append(topLeftState)

        # explore bottom-left state
        bottomLeftState = A_Star_methods.explore_bottomLeft(presentState, grid)
        if bottomLeftState is not None:
            bottomLeftState.heuristic = A_Star_methods.calculateHeuristic(bottomLeftState, goalState)
            # if presentState.heuristic > bottomLeftState.heuristic or bottomLeftState.isVisited is False:
            if bottomLeftState.isVisited is False:
                openList.append(bottomLeftState)

        closedList.append(presentState)

    return None
