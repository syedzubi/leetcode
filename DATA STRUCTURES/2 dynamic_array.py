# 1) INSERT ELEMENT IN THE LAST POSITION OF THE ARRAY

def pushback(self, n):
    if self.length == self.capacity:
        self.resize()

    # insert at next empty position

    self.arr[self.length] = n
    self.length += 1


# since the array is dynamic , when we resize the array , we actually copy all the elements from the old array
# into the new one , and the new array will be double in its size

def resize(self):
    # Create new array of double capacity
    self.capacity = 2 * self.capacity
    newArr = [0] * self.capacity

    # Copy element from the other array

    for i in range(self.length):
        newArr[i] = self.arr[i]
    self.arr = newArr

# 2) REMOVE THE ELEMENT FROM FRONT


def popback(self):
    if self.length > 0:
        self.length -= 1

# 3) GET VALUE AT iTH INDEX


def get(self, i):
    if i < self.length:
        return self.arr[i]

# 4 INSERT n at iTH INDEX


def insert(self, n, i):
    if i < self.length:
        self.arr[i] = n
        return
