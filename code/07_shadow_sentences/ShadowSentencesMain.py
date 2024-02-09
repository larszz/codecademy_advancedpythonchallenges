
def matching_word_lengths(s1: str, s2: str) -> bool:
    words1 = s1.split()
    words2 = s2.split()

    # Check number of words
    if len(words1) != len(words2):
        return False

    # Check word lengths
    for index in range(len(words1)):
        if len(words1[index]) != len(words2[index]):
            return False
    # All matching
    return True


def only_differing_letters(s1: str, s2: str):
    word_chars1 = [set([c for c in w]) for w in s1.split()]
    word_chars2 = [set([c for c in w]) for w in s2.split()]

    for word_index in range(len(word_chars1)):
        for c in word_chars1[word_index]:
            if c in word_chars2[word_index]:
                return False
    return True


def is_shadow(s1: str, s2: str) -> bool:
    return matching_word_lengths(s1, s2) and only_differing_letters(s1, s2)


if __name__ == '__main__':
    print(is_shadow('they are round', 'fold two times'))
    print(is_shadow('they are round', 'fold twr times'))
    print(is_shadow('they are round', 'fold two times times'))
    print(is_shadow('they are round', 'fold two'))
    print(is_shadow('his friends', 'our company'))