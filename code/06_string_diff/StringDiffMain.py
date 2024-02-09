
def find_difference(s1: str, s2: str) -> str:
    l1 = [x for x in s1]

    found_chars = []
    for c in s2:
        if c in l1:
            l1.remove(c)
        else:
            found_chars.append(c)
    if len(found_chars) < 1:
        raise Exception(f"No missing char found in second string (s1: {s1}, s2: {s2})")
    if len(found_chars) > 1:
        raise Exception(f"Found {len(found_chars)} missing chars in s1, should be 1 (s1: {s1}, s2: {s2})")
    return found_chars[0]



if __name__ == '__main__':
    print(find_difference("eueiieo", "iieoedue"))
    # print(find_difference("eueiieo", "eueiieo"))
    # print(find_difference("eueiieo", "eueiieoab"))
