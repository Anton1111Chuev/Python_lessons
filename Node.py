class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next  = next

    def __str__(self):
        return f'value = {self.value} '


class ListNode:

    listNode = []
    headNone = None
    lastNode = None

    def add(self, value):
        node = Node(value)
        ListNode.listNode.append(node)

        if ListNode.lastNode == None:
            ListNode.headNone = node
        else:
            ListNode.lastNode.next = node

        ListNode.lastNode = node

    def __str__(self):
        #res = f'value ={ListNode.headNone.value}   '
        res = ''
        curNode = ListNode.headNone
        while curNode.next != None:
            res = res + f'value ={curNode.value}   '
            curNode = curNode.next

        res = res + f'value = {curNode.value}'
        return res

    @staticmethod
    def revers():

        if ListNode.headNone == None or ListNode.headNone.next == None:
            return

        ListNode.lastNode = ListNode.headNone

        currentNode = ListNode.headNone
        previousNode = None
        nextNode = ListNode.headNone.next

        while currentNode.next != None:
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode  = nextNode
            nextNode = currentNode.next

        currentNode.next = previousNode

        ListNode.headNone = currentNode




listNode = ListNode()
listNode.add(1)
listNode.add(2)
listNode.add(4)
listNode.add(5)


print(listNode)

ListNode.revers()

print(listNode)