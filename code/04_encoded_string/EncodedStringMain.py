

seperator: str = '0'


class PersonalInformation:
    def __init__(self, first: str, last: str, id: str):
        self.first = first
        self.last = last
        self.id = id

    def __str__(self):
        return f'{{ "first_name": "{self.first}", "last_name": "{self.last}", "id": "{self.id} }} '


def get_information(encoded_text: str) -> str:
    parts = encoded_text.split(seperator)
    parts = [part for part in parts if part]
    if len(parts) != 3:
        raise Exception(f"'{encoded_text}': String invalid! Need 3 parts, got {len(parts)}")
    return PersonalInformation(parts[0], parts[1], parts[2]).__str__()


if __name__ == '__main__':
    print(get_information("Robert00000Smith0000000123"))
    print(get_information("Robert00000Smith00000123"))
    print(get_information("Robert0Smith0123"))
    # print(get_information("Robert0Smith0"))
    print(get_information("Robert0Smith0123000"))
    # print(get_information("Robert0Smith0123000AB"))
