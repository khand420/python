class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None
        Node.prev = None


def insertNodeStart(head, newNode):
    newNode.next = head
    head.prev = newNode
    newNode.prev = None
    return head


def insertMiddle(head, newNode):
    temp = head
    while(temp.data != 'c'):
        temp = temp.next 
    buffer =  temp.next 
    temp.next = newNode
    newNode.prev = temp
    newNode.next = buffer
    buffer.prev = newNode
    return head


def insertEnd(head, newNode):
    temp = head
    while(temp.next != None):
        temp.next = newNode
    newNode.prev = temp
    newNode.next = None
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
# nodeE = Node('e')
# nodeF = Node('f')


head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
# nodeD.next = nodeE
# nodeE.next = nodeF

nodeB.next = head
nodeC.next = nodeB
nodeD.next = nodeC


head = insertNodeStart(head,Node('z'))
# head = insertNodeMiddle(head,Node('z'))
# head = insertNodeEnd(head,Node('z'))

printList(head)

