class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def get_mirror(root):
    if(root == None):
        return
    get_mirror(root.left)
    get_mirror(root.right)

    temp=root.left
    root.left=root.right
    root.right=temp

def preorder(root):
    if(root==None):
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


preorder(root)
print(get_mirror(root))
preorder(root)
