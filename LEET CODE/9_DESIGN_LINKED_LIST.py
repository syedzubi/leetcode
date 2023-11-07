class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while 0 < index and cur:
            cur = cur.next
            index -= 1
        
        if cur and cur.next != self.tail and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.head.next, self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev        
        self.print()

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.tail, self.tail.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev        
        self.print()

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while 0 < index and cur:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            node, next , prev = ListNode(val), cur, cur.prev
            next.prev = node
            prev.next = node
            node.next = next
            node.prev = prev        
        self.print()

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while 0 < index and cur:
            cur = cur.next
            index -= 1
        
        if cur and index == 0 and cur != self.tail:
            next, prev = cur.next , cur.prev
            next.prev = prev 
            prev.next = next 

    def print(self):
        curr = self.head.next
        while curr.next:
            print(f'{curr.val} -->', end='')
            curr = curr.next
        print()

obj = MyLinkedList()
obj.addAtHead(10)
obj.addAtHead(20)
obj.addAtHead(30)
obj.addAtHead(40)
obj.addAtHead(50)
obj.addAtTail(57)
obj.addAtTail(540)
obj.addAtTail(512)
obj.addAtTail(740)
obj.addAtTail(4100)
obj.addAtIndex(2, 187)
obj.addAtIndex(6, 1765)
obj.deleteAtIndex(2)
obj.deleteAtIndex(6)