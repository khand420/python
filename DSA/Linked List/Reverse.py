def Reverse(head):
    curr = head
    prev = None
    nextNode = None

    while(curr != None):
        nextNode = curr.next
        curr.next =prev
        prev = curr
        curr = nextNode

    return prev     

