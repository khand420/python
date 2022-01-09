class Node:
    def __init__(Node,data):
        Node.data = data
        Node.next = None


def insertNodeStart(head, newNode):
    newNode.next = head
    head = newNode
    return head


def insertNodeMiddle(head, newNode):
    curr = head 
    while(curr.data != 'e'):
        curr = curr.next

    newNode.next = curr.next
    curr.next = newNode
    return head

def insertNodeEnd(head, newNode):
    curr = head 
    while(curr.data != None):
        curr = curr.next

    newNode.next = curr.next
    curr.next = newNode
    return head  


def printList(head):
    temp = head
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


head = insertNodeStart(head,Node('z'))
# head = insertNodeMiddle(head,Node('z'))
# head = insertNodeEnd(head,Node('z'))

printList(head)



