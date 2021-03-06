class Node:

    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def findSecondMinimumValue( root):
    if root is None:
        return -1
    if root.left == None and root.right == None:
        return -1
    left = root.left.data
    right = root.right.data

    if root.data == root.left.data:
        left = findSecondMinimumValue(root.left)
    if root.data == root.right.data:
        right = findSecondMinimumValue(root.right)

    if left != -1 and right != -1:
        return min(left, right)
    elif left != -1:
        return left
    else:
        return right

root = Node(2)
root.left = Node(3)
root.right = Node(2)
root.right.left = Node(8)
root.right.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(6)
root.left.left.left = Node(3)
root.left.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.right.left.left = Node(20)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
root.right.right.left = Node(2)

print(findSecondMinimumValue( root))

