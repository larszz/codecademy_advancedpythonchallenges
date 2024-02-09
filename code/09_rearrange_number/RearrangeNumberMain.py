

def rearrange(number: int):
    lowest = int(''.join(sorted([c for c in str(number)])))
    highest = int(''.join(sorted([c for c in str(number)], reverse=True)))
    return highest-lowest


if __name__ == '__main__':
    print(str(rearrange(213)))  # -> 198
    print(str(rearrange(938)))  # -> 594
    print(str(rearrange(82749)))  # -> 73953
