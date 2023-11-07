## ZUBAIR SOLUTION

class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


# class Queue:
#     def __init__(self) -> None:
#         self.head = ListNode(-1)
#         self.tail = self.head

#     def enqueue(self, val):
#         node = ListNode(val)
#         node.next = self.head.next
#         self.head.next = node
#         self.view()

#     def dequeue(self):
#         self.head = self.head.next
#         self.view()

#     def view(self):
#         cur = self.head.next
#         while cur:
#             print(f'|{cur.val} -->', end='')
#             cur = cur.next
#         print()

class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.head = self.tail = None
    
    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        if self.tail:
            self.tail.next = newNode
            self.tail = self.tail.next
        # Queue is empty
        else:
            self.head = self.tail = newNode

    def dequeue(self):
        # Queue is empty
        if not self.head:
            return None
        
        # Remove left node and return value
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def print(self):
        cur = self.head
        while cur:
            print(f'|{cur.val} -->', end='')
            cur = cur.next
        print()

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
