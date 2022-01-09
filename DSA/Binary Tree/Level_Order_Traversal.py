class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None


def level_levels(root):
    if(root==None):
        return
    que=[]
    que.append(root)

    while(len(que)>0):
        count=len(que)
        while (count > 0):
            temp = que.pop(0)
            print(temp.data, end=' ')
            if (temp.left):
                que.append(temp.left)
            if (temp.right):
                que.append(temp.right)
            count=count-1
        print("")


# def level_oneLine(root):
#     if(root == None):
#         return

#     que = []
#     que.append(root)

#     while(len(que)>0):
#         temp = que.pop(0)
#         print(temp.data, end=" ")
        
#         if(temp.left):
#             que.append(temp.left)

#         if(temp.right):
#             que.append(temp.right)
                


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.right.left.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)


# level_oneLine(root)
level_levels(root)