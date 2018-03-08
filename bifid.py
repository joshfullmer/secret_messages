from ciphers import Cipher


class Bifid(Cipher):

    def __init__(self, key="BGWKZQPNDSIOAXEFCLUMTHYVR"):
        row_col = [(r, c) for r in range(1, 6) for c in range(1, 6)]
        self.bifid = {char: rc for char, rc in zip(key, row_col)}
        self.reverse = {rc: char for char, rc in self.bifid.items()}

    def encrypt(self, text):
        rows = [self.bifid[char][0] for char in text]
        cols = [self.bifid[char][1] for char in text]
        rows_cols = rows + cols
        new_pairs = [(row, col) for row, col in zip(rows_cols[0::2],
                                                    rows_cols[1::2])]
        return ''.join([self.reverse[pair] for pair in new_pairs])

    def decrypt(self, text):
        # Get the string into a list of tuples
        tups = [self.bifid[char] for char in text]
        # Flatten the list with `list(sum(list_of_tuples, ()))
        nums = list(sum(tups, ()))
        # Split the list in half, then zip the lists to reform the
        # original tuples
        length = int(len(nums) / 2)
        first_half, second_half = nums[:length], nums[length:]
        new_pairs = [(r, c) for r, c in zip(first_half, second_half)]
        # Replace tuples with matches from reverse
        return ''.join([self.reverse[pair] for pair in new_pairs])
