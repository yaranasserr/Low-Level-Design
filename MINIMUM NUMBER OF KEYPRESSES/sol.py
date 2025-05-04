from collections import Counter

def minimum_keypresses(s):
    # Count the frequency of each character
    freq = Counter(s)

    # Sort characters by frequency in descending order
    sorted_freq = sorted(freq.values(), reverse=True)

    # Calculate the minimum number of keypresses
    count = 0
    for index, frequency in enumerate(sorted_freq):
        if index < 9:
            count += frequency * 1
        elif index < 18:
            count += frequency * 2
        else:
            count += frequency * 3

    return count

# First 9 characters → need 1 keypress each
# Next 9 characters → need 2 keypresses each
# Beyond that → need 3 keypresses each
# Unit tests
import unittest

class TestMinimumKeypresses(unittest.TestCase):
    def test_example(self):
        self.assertEqual(minimum_keypresses("geeksforgeeks"), 13)

    def test_single_character(self):
        self.assertEqual(minimum_keypresses("a"), 1)

    def test_all_unique(self):
        self.assertEqual(minimum_keypresses("abcdefghi"), 9)

    def test_repeated_characters(self):
        self.assertEqual(minimum_keypresses("aaaabbbbcccc"), 12)

    def test_large_input(self):
        self.assertEqual(minimum_keypresses("a" * 10 + "b" * 8 + "c" * 5), 23)

    def test_empty_string(self):
        self.assertEqual(minimum_keypresses(""), 0)

if __name__ == "__main__":
    unittest.main()