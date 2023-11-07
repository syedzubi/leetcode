class ListNode:
    def __init__(self, val) -> None:
        self.prev = None
        self.val = val
        self.next = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

    def insertBack(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def removeBack(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr.next:
            print(f'{curr.val} -->', end='')
            curr = curr.next
        print()


dll = DoubleLinkedList()

dll.insertFront(10)
dll.insertFront(20)
dll.insertFront(30)
dll.insertBack(120)
dll.insertBack(980)
dll.removeBack()
