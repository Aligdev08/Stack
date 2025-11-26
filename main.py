from stack import Stack


def display_options() -> None:
    print("")
    print("1 - push")
    print("2 - pop")
    print("3 - peek")
    print("4 - test for empty")
    print("5 - test for full")
    print("6 - display stack")
    print("9 - quit")
    print("")


def is_num(input: str) -> bool:
    try:
        input = int(input)
        return True
    except ValueError:
        return False


max_length = input("What is the stack's length? ")
while not is_num(max_length):
    max_length = input("Please input a valid number: ")

stack = Stack(int(max_length))

choice = -1
while choice != 9:
    display_options()
    choice = input("> ")

    while not is_num(choice):
        print("Please input a valid number.")
        choice = input("> ")

    choice = int(choice)

    match choice:
        case 1:
            value = input("Input a value to push: ")
            stack.push(value)
        case 2:
            print(f"Popped: {stack.pop()}")
        case 3:
            print(f"Peeked {stack.peek()}")
        case 4:
            print(str(stack.is_empty()))
        case 5:
            print(str(stack.is_full()))
        case 6:
            print(stack)
        case 9:
            pass
        case _:  # fallback
            print("Input one of the number options.")
