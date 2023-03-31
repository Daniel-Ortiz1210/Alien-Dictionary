order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["hacen", "hacer"]


def verifying_alien_dictionary(words, order):
    hash_map = {}

    for index, char in enumerate(order):
        hash_map[char] = index
    
    for word_index in range(len(words) - 1):
        for letter_index in range(len(words[word_index])):

            if letter_index + 1 > len(words[word_index+1]):
                break

            if hash_map[words[word_index][letter_index]] > hash_map[words[word_index + 1][letter_index]]:
                return False
    return True
