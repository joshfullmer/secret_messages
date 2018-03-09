from ciphers import Cipher


class Bifid(Cipher):
    """
    Modifies the existing initialize, encrypt, and decrypt methods of Cipher.
    Takes in a string of 25 characters to generate the polybius square required
    for a Bifid cipher.

    https://en.wikipedia.org/wiki/Bifid_cipher
    """

    def __init__(self, key=None):
        """
        Uses the provided string to generate a 5x5 polybius square.

        Creates dictionaries for letter > coord relationship and the
        reverse.
        """

        # Set the default polybius square (which is the example in the wiki)
        if not key:
            key = "BGWKZQPNDSIOAXEFCLUMTHYVR"

        # Create and assign coordinates to each letter in the PB square
        # Also generate the reverse dictionary
        row_col = [(r, c) for r in range(1, 6) for c in range(1, 6)]
        self.bifid = {char: rc for char, rc in zip(key, row_col)}
        self.reverse = {rc: char for char, rc in self.bifid.items()}

    def encrypt(self, text):
        """
        Encrypts the text using a Bifid cipher

        Splits the coordiates into lists by row numbers and column numbers.
        Joins those lists, then recreates letters using new pairs of numbers
        """

        # Bifids using a 5x5 Polybius square have all letters of the latin
        # alphabet except for J, which is replaced with I
        text = text.replace('J', 'I')

        # Turn the provided text into a list of row numbers and column numbers
        rows = [self.bifid[char][0] for char in text]
        cols = [self.bifid[char][1] for char in text]

        # Combine lists
        rows_cols = rows + cols

        # Generate new coordinates by using the even indexes for row numbers
        # and odd indexes for columns
        new_coords = [(row, col) for row, col in zip(rows_cols[0::2],
                                                     rows_cols[1::2])]

        # Reverse match on the cipher to return the encrypted text
        return ''.join([self.reverse[pair] for pair in new_coords])

    def decrypt(self, text):
        """
        Decrypts the text using a Bifid cipher

        Converts text to list of coordinates, flatten list of coordinates,
        then recreate pairs from the first half as row numbers, and the second
        half as column numbers. Then converts coords to letters
        """

        # Get the string into a list of tuples
        tups = [self.bifid[char] for char in text]

        # Flatten the list with `list(sum(list_of_tuples, ()))
        nums = list(sum(tups, ()))

        # Split the list in half, then zip the lists to reform the
        # original tuples
        length = int(len(nums) / 2)
        rows, cols = nums[:length], nums[length:]
        new_coords = [(r, c) for r, c in zip(rows, cols)]

        # Replace tuples with matches from reverse
        return ''.join([self.reverse[pair] for pair in new_coords])
