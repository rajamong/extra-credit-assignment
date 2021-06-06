# imports pytest functionality
import pytest
# imports leapyear program
import reverse # type: ignore


def test1():
    # tests the sentence reversing functionality
    sentence = "this is a practice sentence."
    assert reverse.reverse(sentence) == 'sentence practice a is this.'

def test2():
    # tests the sentence reversing functionality
    sentence = "tHiS iS aLsO a PrAcTiCe SeNtEnCe."
    assert reverse.reverse(sentence) == 'SeNtEnCe PrAcTiCe a aLsO iS tHiS.'


if __name__ == "__main__":
    pytest.main()