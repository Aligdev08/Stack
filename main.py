class Stack:
    def __init__(self, max_length: int):
        self.array = [None] * max_length
        self.top_pointer = 0  # next available index

    def is_empty(self) -> bool:
        return self.top_pointer == 0

    def is_full(self) -> bool:
        return self.top_pointer == len(self.array)

    def peek(self) -> bool:
        return self.array[self.top_pointer - 1]

    def pop(self) -> object:
        if self.is_empty():
            raise ValueError("Stack is empty.")
        self.top_pointer -= 1
        return self.array[self.top_pointer]

    def push(self, value: object) -> None:
        if self.is_full():
            raise ValueError("Stack is full.")
        self.array[self.top_pointer] = value
        self.top_pointer += 1
