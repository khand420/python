class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        lheight = self.height_tree(root.left)
        rheight = self.height_tree(root.right)
        ldiam = self.diameterOfBinaryTree(root.left)
        rdiam = self.diameterOfBinaryTree(root.right)
        a = max(lheight + rheight, max(ldiam, rdiam))
        return a

    def height_tree(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.height_tree(root.left)
            rdepth = self.height_tree(root.right)
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
root = Node(9)
root.left = Node(1)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.right.left.left = Node(8)

s=Solution()
print(s.diameterOfBinaryTree(root))