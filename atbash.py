import string

from ciphers import Cipher


class Atbash(Cipher):
    cipher = {p: c for p, c in zip(string.ascii_uppercase,
                                   string.ascii_uppercase[::-1])}

    def encrypt(self, text):
        return ''.join([self.cipher[char] for char in text.upper()])

    def decrypt(self, text):
        return ''.join([self.cipher[char] for char in text.upper()])
