# imports unittest functionality
import unittest
# imports reverse class from reverse program
from reverse import reverse 

class testCase(unittest.TestCase):
    # tests the sentence reversing functionality
    def test1(self):
        for sentence in ["this is a practice sentence."]:
            assert reverse(sentence) == 'sentence practice a is this.'

    # tests the sentence reversing functionality
    def test2(self):
        for sentence in ["tHiS iS aLsO a PrAcTiCe SeNtEnCe."]:
            assert reverse(sentence) == 'SeNtEnCe PrAcTiCe a aLsO iS tHiS.'


if __name__ == "__main__":
    unittest.main()