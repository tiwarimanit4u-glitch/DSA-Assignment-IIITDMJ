#Assignments-3
def check_n(n):
    if type(n) is not int or n < 0:
        raise ValueError("n must be a non-negative integer")

def factorial(n):
    check_n(n)
    if n == 0:
        return 1
    return n * factorial(n - 1)

def natural_sum(n):
    check_n(n)
    if n == 0:
        return 0
    return n + natural_sum(n - 1)

def power(x, n):
    check_n(n)
    if n == 0:
        return 1
    return x * power(x, n - 1)

def is_sorted(data, index=0):
    if index >= len(data) - 1:
        return True
    if data[index] > data[index + 1]:
        return False
    return is_sorted(data, index + 1)

class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.data[-1]
    
class CircularQueue:
    def __init__(self, capacity=5):
        if type(capacity) is not int or capacity < 1:
            raise ValueError("capacity must be a positive integer")
        self.data = [None] * capacity
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        if self.size == len(self.data):
            raise OverflowError("queue is full")
        index = (self.front + self.size) % len(self.data)
        self.data[index] = element
        self.size += 1

    def first(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.data[self.front]

    def dequeue(self):
        element = self.first()
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return element

    def display(self):
        result = []
        for i in range(self.size):
            result.append(self.data[(self.front + i) % len(self.data)])
        return result

class CircularDeque(CircularQueue):
    def add_first(self, element):
        if self.size == len(self.data):
            raise OverflowError("deque is full")
        self.front = (self.front - 1) % len(self.data)
        self.data[self.front] = element
        self.size += 1

    def add_last(self, element):
        self.enqueue(element)

    def delete_first(self):
        return self.dequeue()

    def delete_last(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        index = (self.front + self.size - 1) % len(self.data)
        element = self.data[index]
        self.data[index] = None
        self.size -= 1
        return element

def main():
    print("PART A, Q2: RECURSIVE FUNCTIONS")
    print("Preconditions: n is an integer >= 0; x is numeric for power.")
    print("Base cases: factorial(0)=1, sum(0)=0, power(x,0)=1.")
    print("factorial(5) =", factorial(5))
    print("natural_sum(10) =", natural_sum(10))
    print("power(2, 10) =", power(2, 10))

    print("\nPART A, Q4: NON-DECREASING ORDER")
    for data in ([], [5], [1, 1, 3], [1, 3, 2]):
        print(data, "->", is_sorted(data))
        
    print("\nPART C, Q2: STACK")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("After push 10, push 20: top =", stack.top(), "length =", len(stack))
    print("Pop:", stack.pop(), "then", stack.pop(), "empty:", stack.is_empty())

    print("\nPART C, Q8: CIRCULAR QUEUE")
    print("Insertion index = (front + size) % len(data).")
    print("After dequeue: front = (front + 1) % len(data).")
    queue = CircularQueue(3)
    for element in (10, 20, 30):
        queue.enqueue(element)
    print("Full queue:", queue.display(), "storage:", queue.data)
    print("Dequeue:", queue.dequeue())
    queue.enqueue(40)
    print("Wrapped queue:", queue.display(), "storage:", queue.data,
          "front:", queue.front, "size:", queue.size)

    print("\nPART C, Q10: CIRCULAR DEQUE")
    print("add_first: front=(front-1)%capacity; store; size+=1.")
    print("add_last: store at (front+size)%capacity; size+=1.")
    print("delete_first: clear front; front=(front+1)%capacity; size-=1.")
    print("delete_last: clear (front+size-1)%capacity; size-=1.")
    deque = CircularDeque(4)
    deque.add_last(20)
    deque.add_first(10)
    deque.add_last(30)
    print("After additions:", deque.display())
    print("delete_first:", deque.delete_first())
    print("delete_last:", deque.delete_last())
    print("Remaining:", deque.display())


if __name__ == "__main__":
    main()
