class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def height_Bt(A):
    if(A==None):
        return 0
    else:
        Ldepth = height_Bt(A.left)

        Rdepth = height_Bt(A.right)

        if(Ldepth > Rdepth):
            return(1+Ldepth)
        else:
            return(1+Rdepth)   


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4) 
root.left.right = Node(5)  
root.left.left.left = Node(7) 
root.right.right = Node(6)  

print("Maximum hieght of Binary Tree is:",height_Bt(root))                      
