class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None


def delNode_start(head):
    if(head==None):
        return

    if(head.next == None):
        return None

    head = head.next 
    return head


def delNode_mid(head, node_to_del):
    temp = head

    while(temp.next.data != node_to_del):
        temp = temp.next 
    temp.next = temp.next.next  
    return head  


def delNode_end(head):
    temp = head

    while(temp.next.next != None):
        temp = temp.next 
    temp.next = None 
    return head  


def printList(head):
    temp =head
    while(temp): 
        print(temp.data)
        temp = temp.next  



head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF


head = delNode_start(head)
head = delNode_mid(head,('c'))
head = delNode_end(head)

printList(head)

    
