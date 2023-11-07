class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
