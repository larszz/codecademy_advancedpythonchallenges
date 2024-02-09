

def get_as_hex_string(text: str):
    hex_chars = [str(hex(ord(c)))[2:] for c in text]
    return ' '.join(hex_chars)


if __name__ == '__main__':
    print(get_as_hex_string('abc def.'))

