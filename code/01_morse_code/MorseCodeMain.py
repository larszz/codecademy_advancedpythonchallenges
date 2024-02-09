from global_objects.DoubleDictionary import DoubleDictionary


def create_morse_dictionary() -> DoubleDictionary:
    codes = DoubleDictionary()
    codes.add('A', '·–')
    codes.add('B', '–···')
    codes.add('C', '–·–·')
    codes.add('D', '–··')
    codes.add('E', '·')
    codes.add('F', '··–·')
    codes.add('G', '––·')
    codes.add('H', '····')
    codes.add('I', '··')
    codes.add('J', '·–––')
    codes.add('K', '–·–')
    codes.add('L', '·–··')
    codes.add('M', '––')
    codes.add('N', '–·')
    codes.add('O', '–––')
    codes.add('P', '·––·')
    codes.add('Q', '––·–')
    codes.add('R', '·–·')
    codes.add('S', '···')
    codes.add('T', '–')
    codes.add('U', '··–')
    codes.add('V', '···–')
    codes.add('W', '·––')
    codes.add('X', '–··–')
    codes.add('Y', '–·––')
    codes.add('Z', '––··')
    codes.add('0', '–––––')
    codes.add('1', '·––––')
    codes.add('2', '··–––')
    codes.add('3', '···––')
    codes.add('4', '····–')
    codes.add('5', '·····')
    codes.add('6', '–····')
    codes.add('7', '––···')
    codes.add('8', '–––··')
    codes.add('9', '––––·')
    codes.add('.', '·–·–·–')
    codes.add(',', '––··––')
    codes.add(' ', ' '*7)
    codes.add('SPACER', ' '*3)
    return codes


def convert_to_morse(codes: DoubleDictionary, text: str) -> str:
    output: str = ""
    for c in text:
        c_upper = c.upper()
        output += codes.get_value(c_upper) + codes.get_value("SPACER")
    return output


if __name__ == '__main__':
    morse_codes = create_morse_dictionary()
    text = input("Give text: ")
    print(convert_to_morse(morse_codes, text))
