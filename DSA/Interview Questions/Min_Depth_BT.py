class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def MinHeight_Bt(root):
    if(root==None):
        return 0
    else:
        Ldepth = MinHeight_Bt(root.left)

        Rdepth = MinHeight_Bt(root.right)

        if(Ldepth > Rdepth):
            return(1+Rdepth) #only changes
        else:
            return(1+Ldepth)   


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4) 
root.left.right = Node(5)  
root.left.left.left = Node(7) 
root.right.right = Node(6)  

print("Minimum hieght of Binary Tree is:",MinHeight_Bt(root))                      
