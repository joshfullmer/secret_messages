from math import gcd

from ciphers import Cipher


class Affine(Cipher):
    """
    Modifies the initialize, encrypt, and decrypt of the Cipher class
    and adds a new 'is_coprime' method to check if provided input is
    a coprime with 26.

    https://en.wikipedia.org/wiki/Affine_cipher
    """

    def __init__(self, a, b):
        """
        Checks if the provided arguments are valid, namely if 'a' is a valid
        coprime with 26, and raises a TypeError if it's not.

        Generates dictionaries for the key, both the forward and backward
        relationship.
        """

        if not self.is_coprime(a):
            coprimes = [i for i in range(26) if self.is_coprime(i)]
            raise TypeError(
                "'a' must be coprime of 26. Possible coprimes: {}".format(
                    coprimes
                ))

        # This method for generating the key is provided on the wikipedia page
        # for the affine cipher:
        # https://en.wikipedia.org/wiki/Affine_cipher#Programming_examples
        self.affine = {chr(i+65): chr(((a*i+b) % 26)+65) for i in range(26)}
        self.reverse = {c: p for p, c in self.affine.items()}

    def encrypt(self, text):
        """
        Use the key created on initialization to encrypt
        """

        return ''.join([self.affine.get(char, '') for char in text])

    def decrypt(self, text):
        """
        Use the reverse of the key created on initialization to decrypt
        """

        return ''.join([self.reverse.get(char, '') for char in text])

    def is_coprime(self, num):
        """
        Uses the math module's greatest common denominator to
        determine if the provided 'a' is a coprime with 26
        """

        return gcd(num, 26) == 1
