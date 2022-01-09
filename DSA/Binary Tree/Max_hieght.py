class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def max_height_binary(A):
    if(A==None):
        return 0
    else:
        ldepth=max_height_binary(A.left)
        rdepth = max_height_binary(A.right)

        if(ldepth > rdepth):
            return 1+ldepth
        else:
            return 1+rdepth






root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(7)
root.right.right = Node(6)

print(max_height_binary(root))
