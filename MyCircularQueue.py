class MyCircularQueue:

    def __init__(self, k: int):
        # tail, head => count (empty or full)
        self.q = [-1 for _ in range(k)]
        self.tail, self.head, self.count, self.k = 0, 0, 0, k
    def enQueue(self, value: int) -> bool:
        if self.count < self.k:
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.k
            self.count += 1
            return True
        return False
    def deQueue(self) -> bool:
        if self.count > 0:
            self.head = (self.head + 1) % self.k
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        if self.count > 0:
            return self.q[self.head]
        return -1

    def Rear(self) -> int:
        if self.count > 0:
            return self.q[self.tail - 1]
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
