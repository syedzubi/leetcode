def push(self, n):
    self.stack.append(n)


def pop(self):
    return self.stack.pop()


def peek(self):
    return self.stack[-1]

# Operation	Big-O Time Complexity	Notes
# Push	      O(1)
# Pop	      O(1)*	                Check if the stack is empty first
# Peek/Top	  O(1)*	                Retrieves without removing
