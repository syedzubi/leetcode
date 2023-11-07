class Heap:
    def __init__(self) -> None:
        self.heap = [0]

    def __str__(self) -> str:
        return str(self.heap[1:])

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and
                        self.heap[2 * i + 1] < self.heap[2 * i] and
                        self.heap[i] > self.heap[2 * i + 1]
                    ):
                self.heap[i], self.heap[2 * i +
                                        1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
                print(f'RIGHT CHILD SWAP LATER:- {str(self.heap[1:])}')
            elif self.heap[i] > self.heap[2*i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
                print(f'LEFT CHILD SWAP LATER:- {str(self.heap[1:])}')
            else:
                break
        return res


h = Heap()
h.push(14)
h.push(19)
h.push(16)
h.push(21)
h.push(26)
h.push(19)
h.push(68)
h.push(65)
h.push(30)
print(h)
h.pop()
print(h)
h.pop()
print(h)
