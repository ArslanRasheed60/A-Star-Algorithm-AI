class StateClass:

    def __int__(self):
        self.x = 0
        self.y = 0
        self.cost = 0
        self.heuristic = 0
        self.parent = None
        self.isVisited = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def calculateTotalCost(self):
        return self.cost + self.heuristic
