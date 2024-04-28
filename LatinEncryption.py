def swap_keys_and_values(input_dict):
    """Return reverse base dict"""

    return {value: key for key, value in input_dict.items()}


# Fix dict
translit_dict = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е',
    'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'й',
    'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
    'p': 'п', 'q': 'к', 'r': 'р', 's': 'с', 't': 'т',
    'u': 'у', 'v': 'в', 'м': 'м', 'x': 'х', 'y': 'ы',
    'z': 'з',
    'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е',
    'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Й',
    'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О',
    'P': 'П', 'Q': 'К', 'R': 'Р', 'S': 'С', 'T': 'Т',
    'U': 'У', 'V': 'В', 'W': 'В', 'X': 'Х', 'Y': 'Ы',
    'Z': 'З',
}


class LatinEncryption:
    """Replaces all Cyrillic with Latin"""

    def __init__(self):
        self.base_dict = swap_keys_and_values(translit_dict)
        self.reverse_base_dict = translit_dict

    def encrypt(self, text):
        result = ""
        for char in text:
            if char in self.base_dict.keys():
                result += self.base_dict[char]
            else:
                result += char

        return result

    def decrypt(self, text):
        result = ""
        for char in text:
            if char in self.reverse_base_dict.keys():
                result += self.reverse_base_dict[char]
            else:
                result += char

        return result
