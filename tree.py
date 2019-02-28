class TreeNode:
    def __init__(self, right= None, left=None,  data = None,parent=None):
        self.right = right
        self.data = data
        self.left = left
        if left is not None:
            self.left.addParent(self)
        if right is not None:
            self.right.addParent(self)
        self.parent = parent

    def hasLeft(self):
        return self.left

    def hasBouth(self):
        return self.right is not None and self.left is not None

    def hasData(self):
        return self.data is not None

    def hasRight(self):
        return self.right

    def search_code(self, data):
        toret = ''
        if self.parent is not None:
            toret += '.' if self.parent.left == self else '_'
        if self.data == data:
            return toret
        else:
            toret1 = self.left.search_code(data) if self.hasLeft() else None
            toret2 = self.right.search_code(data) if self.hasRight() else None
            if toret1 is not None:
                toret += toret1
                return toret
            elif toret2 is not None:
                toret += toret2
                return toret
            else:
                return None


    def addParent(self, parent):
        # if not parent.left:
        #     parent.left = self
        # elif not parent.right:
        #     parent.right = self
        # else:
        #     return False
        self.parent = parent
        return True

    def __repr__(self):
        return "TreeNode({},{},{},{})".format("Object" if isinstance(self.right, TreeNode) else self.right, self.left, self.data, "None" if not isinstance(self.parent, TreeNode) and self.parent is not None else "Obejct")