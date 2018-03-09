import os

from affine import Affine
from atbash import Atbash
from bifid import Bifid
from caesar import Caesar

CIPHER_INPUTS = ['1', 'C', 'CEASAR', '2', 'A', 'ATBASH',
                 '3', 'B', 'BIFID', '4', 'F', 'AFFINE']

PB_SQUARE_CHARS = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu(error=''):
    clear()
    print("Got a message you need encrypted or decrypted? "
          "You've come to the right place!\n")
    print("Here are the list of ciphers you can use:\n")
    print("1. (C)easar")
    print("2. (A)tbash")
    print("3. (B)ifid")
    print("4. A(f)fine\n\n{}".format(error))


def get_cipher():
    while True:
        cipher = input("Which cipher would you like to use? ").upper()
        if cipher in CIPHER_INPUTS:
            if cipher in ['1', 'C']:
                return 'CAESAR'
            elif cipher in ['2', 'A']:
                return 'ATBASH'
            elif cipher in ['3', 'B']:
                return 'BIFID'
            elif cipher in ['4', 'F']:
                return 'AFFINE'
            else:
                return cipher
        else:
            print_menu("Couldn't recognize input")


if __name__ == '__main__':
    while True:
        print_menu()
        cipher_type = get_cipher()

        encrypt_or_decrypt = input("Do you want to (E)ncrypt or (D)crypt? ")
        if encrypt_or_decrypt.upper() in ['ENCRYPT', 'E']:
            encrypt = True
        else:
            encrypt = False

        message = input("What is your message? ").upper()

        if cipher_type == 'CAESAR':
            offset = input("What is your desired offset? "
                           "(blank for default of 3) ")
            try:
                offset = int(offset)
            except ValueError:
                cipher = Caesar()
            else:
                cipher = Caesar(offset)

        if cipher_type == 'ATBASH':
            cipher = Atbash()

        if cipher_type == 'BIFID':
            print("Enter a key below, or just hit Enter to use the default"
                  "key of: BGWKZQPNDSIOAXEFCLUMTHYVR")
            while True:
                key = input(
                    "Enter a string of 25 characters (A-Z minus J): ").upper()
                if not key:
                    break
                if sorted(key) != sorted(PB_SQUARE_CHARS):
                    print("Key must have each letter of the alphabet, minus J")
                    continue
                if len(key) != 25:
                    print("Key must have 25 characters (A-Z minus J)")
                    continue
                break
            cipher = Bifid(key)

        if cipher_type == 'AFFINE':
            print("An Affine cipher uses the following formula to generate "
                  "a key: V = (ax + b) mod 26")
            a = input("Please provide 'a': ")
            b = input("Please provide 'b': ")
            while True:
                if not a:
                    print("'a' must be a number")
                    a = input("Please provide 'a': ")
                    continue
                if not b:
                    print("'b' must be a number")
                    b = input("Please provide 'b': ")
                    continue
                try:
                    a = int(a)
                except ValueError:
                    print("'a' must be a number")
                    a = input("Please provide 'a': ")
                    continue
                try:
                    b = int(b)
                except ValueError:
                    print("'b' must be a number")
                    b = input("Please provide 'b': ")
                    continue
                try:
                    cipher = Affine(a, b)
                except TypeError as ve:
                    print(ve)
                    a = input("Please provide 'a': ")
                    continue
                break

        if encrypt:
            print("Encrypted string: {}".format(cipher.encrypt(message)))
        else:
            print("Decrypted string: {}".format(cipher.decrypt(message)))

        again = input("Encrypt or decrypt something else? (Y/n) ").upper()
        if again == 'N':
            break
