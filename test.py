import unittest
from csv_converter import buildAddress


class TestHelperFuncs(unittest.TestCase):
    def test_buildAddress(self):
        rowToConvert = ["Dr.", "James", "Jameson", "MD", "123 Main", "Hope", "Wake", "NC", "21213", "123", "456"]
        builtAddress = buildAddress(rowToConvert)
        refAddress = "123 Main Hope, NC"
        self.assertEqual(builtAddress, refAddress)

if __name__ == '__main__':
    unittest.main()
