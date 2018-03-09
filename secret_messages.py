import os
import re

from affine import Affine
from atbash import Atbash
from bifid import Bifid
from caesar import Caesar

CIPHER_INPUTS = ['1', 'C', 'CEASAR', '2', 'A', 'ATBASH',
                 '3', 'B', 'BIFID', '4', 'F', 'AFFINE',
                 '', 'X', 'EXIT']

PB_SQUARE_CHARS = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def clear():
    """
    Clears the screen for a clean menu

    Looks at OS version, making it compatible for all OS's.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu(error=''):
    """
    Prints the menu, primarily to be used in a while loop
    """

    clear()
    print("Got a message you need encrypted or decrypted? "
          "You've come to the right place!\n")
    print("Here are the list of ciphers you can use:\n")
    print("1. (C)easar")
    print("2. (A)tbash")
    print("3. (B)ifid")
    print("4. A(f)fine\n")
    print("OR\n\nE(x)it\n{}".format(error))


def get_cipher():
    """
    Takes one of any number of possible inputs (listed in CIPHER_INPUTS)
    and converts them to something that's easy to do logic on.
    """

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
            elif cipher in ['X', '']:
                return 'EXIT'
            else:
                return cipher
        else:
            print_menu("Couldn't recognize input")


def remove_non_alpha(text):
    """
    Ciphers that use transposition don't support numbers, punctuation, or any
    other non-alphabet characters.

    Rather than detect which support them and which don't, all non-alpha
    characters are stripped.
    """

    return re.sub(r'[^A-Za-z]+', '', text)


if __name__ == '__main__':
    while True:

        # Primary menu creation and input
        print_menu()
        cipher_type = get_cipher()
        if cipher_type == 'EXIT':
            break

        # Take an input for encrypt or decrypt and translate to boolean
        encrypt_or_decrypt = input("Do you want to (E)ncrypt or (D)crypt? ")
        if encrypt_or_decrypt.upper() in ['ENCRYPT', 'E']:
            encrypt = True
        else:
            encrypt = False

        # Takes the message input and converts to uppercase
        message = remove_non_alpha(input("What is your message? ")).upper()

        # CAESAR
        # =====================================================================

        if cipher_type == 'CAESAR':
            offset = input("What is your desired offset? "
                           "(blank for default of 3) ")

            # If an int isn't provided, use the default of 3
            # Could be changed to again prompt for a number
            try:
                offset = int(offset)
            except ValueError:
                cipher = Caesar()
            else:
                cipher = Caesar(offset)

        # ATBASH
        # =====================================================================

        # No input necessary to generate key
        if cipher_type == 'ATBASH':
            cipher = Atbash()

        # BIFID
        # =====================================================================

        if cipher_type == 'BIFID':
            print("Enter a key below, or just hit Enter to use the default "
                  "key of: BGWKZQPNDSIOAXEFCLUMTHYVR")
            while True:
                key = input(
                    "Enter a string of 25 characters (A-Z minus J): ").upper()

                # Handles the case where user wants to use default key
                if not key:
                    break

                # Checks if input contains the entire alphabet minus the letter
                # J
                if sorted(key) != sorted(PB_SQUARE_CHARS):
                    print("Key must have each letter of the alphabet, minus J")
                    continue
                break

            cipher = Bifid(key)

        # AFFINE
        # =====================================================================

        if cipher_type == 'AFFINE':
            print("An Affine cipher uses the following formula to generate "
                  "a key: V = (ax + b) mod 26")
            a = input("Please provide 'a': ")
            b = input("Please provide 'b': ")
            while True:

                # Checks if a and/or b are present
                if not a:
                    print("'a' must be a number")
                    a = input("Please provide 'a': ")
                    continue
                if not b:
                    print("'b' must be a number")
                    b = input("Please provide 'b': ")
                    continue

                # Checks if a and/or be are integers
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

                # Checks if a is coprime with 26
                try:
                    cipher = Affine(a, b)
                except TypeError as ve:
                    print(ve)
                    a = input("Please provide 'a': ")
                    continue
                break

        # One-time pad
        pad_key = remove_non_alpha(
            input("Provide One-time Pad (letters only, hit Enter to skip): ")
            ).upper()

        # Output results
        encrypt_type = "Encrypted" if encrypt else "Decrypted"
        if encrypt:

            # Encrypt the string, apply one-time pad, then split into chunks
            # of five characters
            message = cipher.one_time_pad(cipher.encrypt(message),
                                          pad_key,
                                          encrypt)
            message = cipher.chunks_of_five(message)
            encrypt_type = "Encrypted"
        else:

            # Remove one-time pad, then decrypt the string
            message = cipher.decrypt(cipher.one_time_pad(message,
                                                         pad_key,
                                                         encrypt))
            encrypt_type = "Decrypted"
        print("{} string: {}".format(encrypt_type, message))

        # Restart loop on user input
        again = input("Encrypt or decrypt something else? (Y/n) ").upper()
        if again == 'N':
            break
