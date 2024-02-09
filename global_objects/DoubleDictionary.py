

class DoubleDictionary:

    normal_dict: dict
    reverse_dict: dict

    def __init__(self):
        self.normal_dict = {}
        self.reverse_dict = {}

    def add(self, key, value):
        self.normal_dict[key] = value
        self.reverse_dict[value] = key

    def get_value(self, key):
        return self.normal_dict[key]

    def get_key(self, value):
        return self.reverse_dict[value]

    def remove_key(self, key):
        _, value = self.normal_dict.pop(key)
        self.reverse_dict.pop(value)

    def remove_value(self, value):
        _, key = self.reverse_dict.pop(value)
        self.normal_dict.pop(key)