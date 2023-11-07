class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def removeWithIndex(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        # u always start with head.next as u don't want to print the dummy value (-1)
        curr = self.head.next
        while curr:
            print(f'{curr.val} -->', end='')
            curr = curr.next
        print()  # you add this for space between multiple execution of code as we r using end= ''
