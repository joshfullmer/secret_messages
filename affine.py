from math import gcd

from ciphers import Cipher


class Affine(Cipher):

    def __init__(self, a, b):
        if not self.is_coprime(a):
            coprimes = [i for i in range(26) if self.is_coprime(i)]
            raise TypeError(
                "'a' must be coprime of 26. Possible coprimes: {}".format(
                    coprimes
                ))
        self.affine = {chr(i+65): chr(((a*i+b) % 26)+65) for i in range(26)}
        self.reverse = {c: p for p, c in self.affine.items()}

    def encrypt(self, text):
        return ''.join([self.affine.get(char, '') for char in text])

    def decrypt(self, text):
        return ''.join([self.reverse.get(char, '') for char in text])

    def is_coprime(self, num):
        return gcd(num, 26) == 1
