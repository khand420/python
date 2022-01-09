class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def flatten(root):
    if root is not None:
        flatten(root.left)
        flatten(root .right)

        if root.left is not None:
            current = root.left
            
            while current.right is not None:
               current = current.right

            current.right = root.right
            root.right = root.left
            root.left = None

    return root



def printPreOrder(root):
    if root is None:
        return

    print(root.data)
    printPreOrder(root.left)
    printPreOrder(root.right)



root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("e")
root.left.right = Node("f")
root.right.right = Node("g")

flatten(root)
print(printPreOrder(root))