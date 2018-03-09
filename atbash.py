import string

from ciphers import Cipher


class Atbash(Cipher):
    """
    The Atbash cipher doesn't require any user input to generate the key,
    so it is not included in initialization.

    Only overwrites the Cipher class's encrypt and decrypt methods.

    https://en.wikipedia.org/wiki/Atbash
    """

    cipher = {p: c for p, c in zip(string.ascii_uppercase,
                                   string.ascii_uppercase[::-1])}

    def encrypt(self, text):
        """
        Uses the Atbash cipher to encrypt the provided message
        """

        return ''.join([self.cipher.get(char, ' ') for char in text.upper()])

    def decrypt(self, text):
        """
        Uses the Atbash cipher to encrypt the provided message

        The nature of the Atbash cipher means encrypting and decrypting are the
        same, so encrypt is called.
        """

        return self.encrypt(text)
