class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None


def rightView(root, level, max_level):
    if(root != None):
        if(max_level[0] < level):
            print(root.data)
            max_level[0] = level

        rightView(root.right, level + 1, max_level)
        rightView(root.left, level + 1, max_level)


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.right.left = Node('d')
root.right.right = Node('e')


max_level = [0]
print(rightView(root, 1,max_level))
       