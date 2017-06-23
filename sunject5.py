# 写一个 Queue 类，它有两个方法，用法如下


class Queue():
    def __init__(self):
        self.list = []

    def enqueue(self, i):
        self.list.append(i)

    def dequeue(self):
        if self.list:
            return self.list.pop(0)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.dequeue())  # 3
