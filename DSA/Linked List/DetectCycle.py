class Node:
    def __init__(Node,data):
        Node.data = data
        Node.next = None



def detectCycle(head):
    fast = head 
    slow = head
    loopExist = 0

    while(fast!=None and slow!=None and fast.next!=None):
        fast = fast.next.next 
        slow.next 
        if(fast == slow):
            loopExist = 1
            break

        if(loopExist):
            slow = head 
            while(slow != fast):
                slow = slow.next 
            return slow
        return None


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
nodeG = Node('g')
nodeH = Node('h')
nodeI = Node('i')
nodeJ = Node('j')



head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
nodeH.next = nodeI
nodeI.next = nodeJ
nodeJ.next = nodeD




head = detectCycle(head)
printList(head)
    

