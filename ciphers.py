from itertools import cycle
import string


class Cipher:

    # Create the standard letter to number relationship,
    # mapping A-Z to numbers from 0 to 25
    pad = {c: n for c, n in zip(string.ascii_uppercase, range(26))}
    pad_rev = {n: c for c, n in pad.items()}

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
