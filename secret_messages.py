import os

from atbash import Atbash
from caesar import Caesar

CIPHER_INPUTS = ['1', 'C', 'CEASAR', '2', 'A', 'ATBASH',
                 '3', 'B', 'BIFID', '4', 'F', 'AFFINE']


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


def print_message(encrypt, message):
    if encrypt:
        en_or_de = "Encrypted"
    else:
        en_or_de = "Decrypted"
    print("{} string: {}\n".format(en_or_de, message))


if __name__ == '__main__':
    while True:
        print_menu()
        cipher_type = get_cipher()

        message = input("What is your message? ").upper()

        encrypt_or_decrypt = input("Do you want to (E)ncrypt or (D)crypt? ")
        if encrypt_or_decrypt.upper() in ['ENCRYPT', 'E']:
            encrypt = True
        else:
            encrypt = False

        if cipher_type == 'CAESAR':
            offset = input("What is your desired offset? "
                           "(blank for default of 3) ")
            try:
                offset = int(offset)
            except ValueError:
                cipher = Caesar()
            else:
                cipher = Caesar(offset)

            if encrypt:
                print_message(encrypt, cipher.encrypt(message))
            else:
                print_message(encrypt, cipher.decrypt(message))

        if cipher_type == 'ATBASH':
            cipher = Atbash()
            if encrypt:
                print_message(encrypt, cipher.encrypt(message))
            else:
                print_message(encrypt, cipher.decrypt(message))

        again = input("Encrypt or decrypt something else? (Y/n) ").upper()
        if again == 'N':
            break
