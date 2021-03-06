class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None




def spiral_traversal(root):
    if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    result = []
    curr_res = []
    while (s1 or s2):
        while (len(s1) > 0):
            curr = s1[-1]
            curr_res.append(curr.data)
            s1.pop()

            if (curr.left):
                s2.append(curr.left)
            if (curr.right):
                s2.append(curr.right)
            if (len(s1) == 0):
                result.append(curr_res)
                curr_res = []
        while (len(s2) > 0):
            curr = s2[-1]
            curr_res.append(curr.data)
            s2.pop()
            if (curr.right):
                s1.append(curr.right)
            if (curr.left):
                s1.append(curr.left)
            if (len(s2) == 0):
                result.append(curr_res)
                curr_res = []
    return result



root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("e")
root.left.right = Node("f")
root.right.right = Node("g")


print("Sprial Travesal of Binary Tree: ", spiral_traversal(root))    