class CaesarEncryptor:
    # Dictionary that maps each alphabet to its corresponding set of characters
    ALPHABETS = {
        'cyrillic': 'йцукенгшщзхъфывапролджэячсмитьбю',
        'latin': 'abcdefghijklmnopqrstuvwxyz'
    }

    def __init__(self, shift, alphabet='cyrillic'):
        """
        Initializes the CaesarEncryptor with a shift and an alphabet.

        :param shift: The number of positions to shift each character.
        :param alphabet: The alphabet to use for encryption ('cyrillic' or 'latin').
        """
        if alphabet not in self.ALPHABETS:
            raise ValueError(f"Unsupported alphabet. Choose from: {', '.join(self.ALPHABETS.keys())}")
        self.shift = shift
        self.alphabet_lower = self.ALPHABETS[alphabet]
        self.alphabet_upper = self.alphabet_lower.upper()
        self.len_alphabet = len(self.alphabet_lower)

    def _shift_char(self, char, shift):
        """
        Shifts a single character by the specified number of positions.

        :param char: The character to shift.
        :param shift: The number of positions to shift the character.
        :return: The shifted character or the original character if it is not in the alphabet.
        """
        if char in self.alphabet_lower:
            idx = self.alphabet_lower.find(char)
            return self.alphabet_lower[(idx + shift) % self.len_alphabet]
        elif char in self.alphabet_upper:
            idx = self.alphabet_upper.find(char)
            return self.alphabet_upper[(idx + shift) % self.len_alphabet]
        else:
            return char

    def encrypt(self, text):
        """
        Encrypts the text by shifting characters forward.

       :param text: The text to encrypt.
       :return: The encrypted text.
       """
        return ''.join(self._shift_char(c, self.shift) for c in text)

    def decrypt(self, text):
        """
        Decrypts the text by shifting characters backward.

        :param text: The text to decrypt.
        :return: The decrypted text.
        """
        return ''.join(self._shift_char(c, -self.shift) for c in text)

