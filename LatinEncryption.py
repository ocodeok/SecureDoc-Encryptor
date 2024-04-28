def swap_keys_and_values(input_dict):
    """Return reverse base dict"""

    return {value: key for key, value in input_dict.items()}


translit_dict = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е',
    'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'й',
    'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
    'p': 'п', 'q': 'к', 'r': 'р', 's': 'с', 't': 'т',
    'u': 'у', 'v': 'в', 'w': 'в', 'x': 'х', 'y': 'ы',
    'z': 'з',
    'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е',
    'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Й',
    'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О',
    'P': 'П', 'Q': 'К', 'R': 'Р', 'S': 'С', 'T': 'Т',
    'U': 'У', 'V': 'В', 'W': 'В', 'X': 'Х', 'Y': 'Ы',
    'Z': 'З'
}


class LatinEncryption:
    def __init__(self):
        self.base_dict = swap_keys_and_values(translit_dict)
        self.reverse_base_dict = translit_dict

    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass
