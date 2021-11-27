historyStates = set()
goalNodes = []
goalFound = False


class Node:
    global historyStates, goalFound, goalNodes

    def __init__(self, parent=None, value=None, children=None, goalState=False, cost=None, level=None, totalCost=None):

        if goalState is not None and (goalState is True or goalState is False):
            self.goalState = goalState
        else:
            self.goalState = None
        # initialize parent variable for each node
        if parent is not None:
            self.parent = parent
            historyStates.add(parent.value)
        else:
            self.parent = None
            self.totalCost = 0
        # initialize value variable for each node
        if value is not None:
            self.value = value

        else:
            self.value = None

        if cost is not None:
            self.cost = cost
        else:
            tmpVal = abs(self.value.index('b') - parent.value.index('b'))
            if tmpVal == 1 or tmpVal == 2:
                self.cost = 1
            else:
                self.cost = 2

        if level is not None:
            self.level = level
        else:
            self.level = None
        if parent is not None:
            self.totalCost = self.parent.totalCost + self.cost
        else:
            self.totalCost = 0

        # initialize children variable for each node
        if children is not None:
            self.children = children
        else:
            self.children = []

    def findChildren(self):
        global historyStates
        historyStates.add(self.value)
        indxOfB = self.value.index('b')
        if indxOfB == 0:
            tmpstr = self.value
            for i in range(1, 4):
                tmpstr = list(self.value)
                tmpstr[i], tmpstr[0] = tmpstr[0], tmpstr[i]
                tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
                if not (tmpNode.value in historyStates):
                    self.children.append(tmpNode)
                    historyStates.add(tmpNode.value)

        if indxOfB == 6:
            tmpstr = self.value
            for i in range(5, 2, -1):
                tmpstr = list(self.value)
                tmpstr[i], tmpstr[6] = tmpstr[6], tmpstr[i]
                tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
                if not (tmpNode.value in historyStates):
                    self.children.append(tmpNode)
                    historyStates.add(tmpNode.value)

        if indxOfB == 1:
            tmpstr = list(self.value)
            tmpstr[0], tmpstr[1] = tmpstr[1], tmpstr[0]
            tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
            if not (tmpNode.value in historyStates):
                self.children.append(tmpNode)
                historyStates.add(tmpNode.value)
            for i in range(4, 1, -1):
                tmpstr = list(self.value)
                tmpstr[i], tmpstr[1] = tmpstr[1], tmpstr[i]
                tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
                if not (tmpNode.value in historyStates):
                    self.children.append(tmpNode)
                    historyStates.add(tmpNode.value)

        if indxOfB == 5:
            tmpstr = list(self.value)
            tmpstr[6], tmpstr[5] = tmpstr[5], tmpstr[6]
            tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
            if not (tmpNode.value in historyStates):
                self.children.append(tmpNode)
                historyStates.add(tmpNode.value)
            for i in range(2, 5):
                tmpstr = list(self.value)
                tmpstr[i], tmpstr[5] = tmpstr[5], tmpstr[i]
                tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
                if not (tmpNode.value in historyStates):
                    self.children.append(tmpNode)
                    historyStates.add(tmpNode.value)

        if indxOfB == 2:
            tmpstr = list(self.value)
            for i in range(0, 6):
                if i != 2:
                    tmpstr = list(self.value)
                    tmpstr[i], tmpstr[2] = tmpstr[2], tmpstr[i]
                    tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
                    if not (tmpNode.value in historyStates):
                        self.children.append(tmpNode)
                        historyStates.add(tmpNode.value)

        if indxOfB == 4:
            tmpstr = list(self.value)
            for i in range(1, 7):
                if i != 4:
                    tmpstr = list(self.value)
                    tmpstr[i], tmpstr[4] = tmpstr[4], tmpstr[i]
                    tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
                    if not (tmpNode.value in historyStates):
                        self.children.append(tmpNode)
                        historyStates.add(tmpNode.value)

        if indxOfB == 3:
            tmpstr = self.value
            for i in range(0, 7):
                if i != 3:
                    tmpstr = list(self.value)
                    tmpstr[i], tmpstr[3] = tmpstr[3], tmpstr[i]
                    tmpNode = Node(parent=self, value=("".join(tmpstr)), level=self.level + 1)
                    if not (tmpNode.value in historyStates):
                        self.children.append(tmpNode)
                        historyStates.add(tmpNode.value)

    def getChildren(self):
        if len(self.children) > 0:
            return self.children
        self.findChildren()
        return self.children

    def getChildrenValues(self):
        tmp = []
        self.getChildren()

        for x in self.children:
            tmp.append(x.value)
        return tmp

    def isGoal(self):
        global goalFound, goalNodes
        gCount = 0
        for i in self.value:
            if gCount >= 3:
                self.goalState = True
                goalNodes.append(self)
                return True
            if gCount < 3 and i == 'g':
                gCount += 1
            elif gCount < 3 and i == 'r':
                self.goalState = False
                return False

    def checkChildrenNodes(self):
        if self.isGoal():
            return
        goalCount = 0
        for node in self.children:
            if node.isGoal():
                goalCount += 1
        return goalCount

    @staticmethod
    def getHistory():
        return historyStates
