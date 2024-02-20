class MyQueue:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        tmp = self.list[0]
        self.list.pop(0)
        return tmp

    def peek(self) -> int:
        return self.list[0]

    def empty(self) -> bool:
        return self.list == []
