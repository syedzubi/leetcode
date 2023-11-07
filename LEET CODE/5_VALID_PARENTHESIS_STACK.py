def isValid(s: str) -> bool:
    closeToOpen = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False

# The trick in this question is that to use a dictionary - hashMap to store and make use of stack

# if stack is not empty and the bracket that ur trying to access is the closed one of } ) ] then pop the stack
