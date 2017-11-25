import unittest
from . import compiler

class TestChordMethods(unittest.TestCase):
    def test_compiler_chord_to_text(self):
        data = compiler.compile_chord_to_text(length=120, phoneme="aa", chord=[261, 0, 0, 0, 0, 349, 0, 0, 0, 440, 0, 0])
        self.assertEqual(data, ["aa<261,120>","aa<349,120>","aa<440,120>"])

if __name__ == '__main__':
    unittest.main()