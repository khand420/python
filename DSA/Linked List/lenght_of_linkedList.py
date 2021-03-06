
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None


# iterative way 
def length(head):
    tempNode = head
    count = 0
    while(tempNode != None):
        count = count+1
        tempNode = tempNode.next
    print(count)    


# Recursive Way
def length_recur(node):
    if(node == None):
        return 0
    else:
        return 1 + length_recur(node.next)    



head = ListNode('d')
node2 = ListNode('g')
node3 = ListNode('r')
node4 = ListNode('o')

head.next = node2
node2.next = node3
node3.next = node4
node4.next = None
