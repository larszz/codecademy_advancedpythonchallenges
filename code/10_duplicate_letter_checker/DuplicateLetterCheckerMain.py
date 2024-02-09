

def has_duplicate_letter(text: str) -> bool:
    text = text.lower()
    for i in range(len(text)-1):
        # skip whitespace
        if text[i].isspace():
            continue
        if text[i] == text[i+1]:
            return True
    return False


if __name__ == '__main__':
    print(has_duplicate_letter("aabc def"))
    print(has_duplicate_letter("Aabc def"))
    print(has_duplicate_letter("Abc def abcde"))
    print(has_duplicate_letter("abc   def"))
    print(has_duplicate_letter("Abc Abc Abc"))

