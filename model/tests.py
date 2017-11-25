import unittest
from .objects import Chord
from .data import *

TEST_FREQ = [int((440.0 / 32) * (2 ** ((x - 9) / 12))) for x in range(36, 73)]


class TestChordMethods(unittest.TestCase):
    def test_setup(self):
        chord = Chord(choral_id="000106b_", event="1", octave=4, bass_octave=1,
                      pitch_class_mask=["YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO"],
                      bass="F", meter=3, chord_label="F_M")
        self.assertEqual(chord.pitch_class_mask, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0])

    def test_eq(self):
        chord_a = Chord(choral_id="000106b_", event="1", octave=4, bass_octave=1,
                      pitch_class_mask=["YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO"],
                      bass="F", meter=3, chord_label="F_M")
        chord_b = Chord(choral_id="000106b_", event="1", octave=4, bass_octave=1,
                      pitch_class_mask=["YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO"],
                      bass="F", meter=3, chord_label="F_M")
        self.assertTrue(chord_a == chord_b)

    def test_get_chord(self):
        chord = Chord(choral_id="000106b_", event=1, octave=4, bass_octave=1,
                      pitch_class_mask=["YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO"],
                      bass="F", meter=3, chord_label="F_M")
        notes = chord.get_chord(TEST_FREQ)
        self.assertEqual(notes, [261, 0, 0, 0, 0, 349, 0, 0, 0, 440, 0, 0])

    def test_get_bass(self):
        chord = Chord(choral_id="000106b_", event="1", octave=4, bass_octave=1,
                      pitch_class_mask=["YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO"],
                      bass="F", meter=3, chord_label="F_M")
        # ДОДЕЛАЙЁ


class TestDataManipulations(unittest.TestCase):
    def test_format_data(self):
        data = format_data(["000106b_,1,YES, NO, NO, NO, NO,YES, NO, NO, NO,YES, NO, NO,F,3, F_M"])
        self.assertEqual(data,
                         [["000106b_", "1", "YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO",
                           "F", "3", "F_M"]])

    def test_data_to_objects(self):
        objects = data_to_objects(
            [["000106b_", "1", "YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO",
              "F", "3", "F_M"]], octave=4, bass_octave=1)
        self.assertEqual(objects[0].pitch_class_mask, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0])


if __name__ == '__main__':
    unittest.main()
