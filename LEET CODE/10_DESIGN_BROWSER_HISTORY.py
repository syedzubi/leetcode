# THIS IS NOT AN EFFICIENT SOLUTION , hence 239ms and 18.96MB

# class ListNode:
#     def __init__(self, val, prev=None, next=None) -> None:
#         self.prev = prev
#         self.val = val
#         self.next = next

# class BrowserHistory:

#     def __init__(self, homepage: str) -> None:
#         self.cur = ListNode(homepage)

#     def visit(self, url: str):
#         self.cur.next = ListNode(url, self.cur)
#         self.cur = self.cur.next

#     def back(self, steps: int):
#         while self.cur.prev and steps > 0:
#             self.cur = self.cur.prev
#             steps -= 1
#         return self.cur.val

#     def forward(self, steps: int):
#         while self.cur.next and steps > 0:
#             self.cur = self.cur.next
#             steps -= 1
#         return self.cur.val

# ANOTHER APPROACH --->>> MOST OPTIMAL SOLUTION 199ms and 18.92MB
# class BrowserHistory:

#     def __init__(self, homepage: str) -> None:
#         self.i = 0
#         self.len = 1
#         self.history = [homepage]

#     def visit(self, url: str):
#         if len(self.history) < self.i + 2:
#             self.history.append(url)
#         else:
#             self.history[self.i + 1] = url

#         self.i += 1
#         self.len = self.i + 1

#     def back(self, steps: int):
#         self.i = max(self.i - steps, 0)
#         return self.history[self.i]

#     def forward(self, steps: int):
#         self.i = min(self.i + steps, self.len - 1)
#         return self.history[self.i]
