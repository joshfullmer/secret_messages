from itertools import cycle
import random
import string


class Cipher:

    # Create the standard letter to number relationship,
    # mapping A-Z to numbers from 0 to 25
    pad = {c: n for c, n in zip(string.ascii_uppercase, range(26))}
    pad_rev = {n: c for c, n in pad.items()}

    # Garbage characters to add padding for chunks of 5
    GARBAGE = "0123456789!\"#$%&\'()*+,-./:;<=>?@\\]^_`{|}~"

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def one_time_pad(self, text, key, encrypt):
        """
        Implements a one-time pad on a string, using a given key of letters

        Uses the 'encrypt' boolean to determine if the key needs to be
        added or subtracted from the text

        https://en.wikipedia.org/wiki/One-time_pad
        """

        # Allows the user to not use a one-time pad
        if not key:
            return text

        # Determines if the key needs to be added to the message or
        # subtracted
        if not encrypt:
            negate = -1
        else:
            negate = 1

        # Converts the characters to numbers
        text_nums = [self.pad[c] for c in text]
        key_nums = [self.pad[c] * negate for c in key]

        # Combines the two numbers (using a repeating zip, if the key isn't
        # as long as the message) and does a modulo 26 operation to ensure
        # the resulting number is between 0 and 25, corresponding to a letter
        text_plus_key = [(t + k) % 26 for t, k in zip(text_nums,
                                                      cycle(key_nums))]

        # Converts the numbers back to letters using the reverse relationship
        padded_text = ''.join([self.pad_rev[n] for n in text_plus_key])
        return padded_text

    def chunks_of_five(self, text):
        """
        Splits the encrypted string into blocks of 5, separated by a space
        and adds garbage characters as padding if the length of the string
        is not a multiple of 5
        """

        # Gets a random index in the length of the string and adds a random
        # garbage character at that index
        while len(text) % 5 != 0:
            rand_index = random.randint(0, len(text)-1)
            garb_char = random.choice(self.GARBAGE)
            text = text[:rand_index] + garb_char + text[rand_index:]

        # Generate list of indeces where the 5 chars should start
        # then get all 5 chars and join with a space
        text = ' '.join([text[i:i+5] for i in range(0, len(text), 5)])
        return text
