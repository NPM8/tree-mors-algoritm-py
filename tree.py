class TreeNode:
    def __init__(self, right= None, data = None, left=None, parent=None):
        self.right = right
        self.data = data
        self.left = left
        self.parent = parent

    def hasLeft(self):
        return self.left

    def hasBouth(self):
        return self.right and self.left

    def hasData(self):
        return self.data

    def hasRight(self):
        return self.right

    def search(self, data):
        toret = ''
        if self.parent is not None:
            toret += '.' if self.parent.left.data == self.data else '_'
        if self.data == data:
            return toret
        else:
            toret1 = self.left.search(data)
            toret2 = self.right.search(data)
            if toret1 is not None:
                toret += toret1
                return toret
            elif toret2 is not None:
                toret += toret2
                return toret


    def addParent(self, parent):
        if not parent.left:
            parent.left = self
        elif not parent.right:
            parent.right = self
        else:
            return False
        self.parent = parent
        return True

    def __repr__(self):
        return "TreeNode({},{},{})".format("Object" if isinstance(self.right, TreeNode) else self.right, self.left, "None" if not isinstance(self.parent, TreeNode) and self.parent is not None else "Obejct")