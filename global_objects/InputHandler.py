

def get_input(message: str) -> str:
    return input(message)


def get_numeric_input(message: str) -> int:

    number: int | None = None
    while not number:
        read_text = get_input(message)
        if read_text.isnumeric():
            number = int(read_text)
            break
        else:
            print(f"'{read_text}': Text is not numeric, please enter a number")
    return number

