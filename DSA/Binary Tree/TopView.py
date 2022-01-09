class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def top_view(root):
    if root is not None:
        dict = {}
        node_dict = {}
        que = list()
        que.append(root)
        node_dict[root.data] = 0
        while len(que) > 0:
            temp = []
            curr = que.pop(0)
            if curr is not None:
                level = node_dict[curr.data]
                if level not in dict:
                    temp.append(curr.data)
                    dict[level] = temp

                if curr.left is not None:
                    left_node = curr.left
                    que.append(left_node)
                    node_dict[left_node.data] = node_dict[curr.data] - 1
                if curr.right is not None:
                    right_node = curr.right
                    que.append(right_node)
                    node_dict[right_node.data] = node_dict[curr.data] + 1
        print(dict)



root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.right.left = Node('f')
root.right.right = Node('g')
root.left.left = Node('d')
root.left.right = Node('e')



top_view(root)
       