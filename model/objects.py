"""
TODO:
- методы
"""


class Chord(object):
    """
    Choral ID: corresponding to the file names from (Bach Central)[[Web Link]].
    Event: index (starting from 1) of the event inside the chorale.
    Pitch class mask: mask of used notes(1 - used, 2 - not used)
    Bass: Pitch class of the bass note
    Meter: integers from 1 to 5. Lower numbers denote less accented events,
    higher numbers denote more accented events.
    Chord label: Chord resonating during the given event.
    """
    __slots__ = ['choral_id', 'event', 'pitch_class_mask', 'octave', 'bass', 'bass_octave', 'meter', 'chord_label']

    def __init__(self, choral_id, event, pitch_class_mask, octave, bass, bass_octave, meter, chord_label):
        self.choral_id = choral_id
        self.event = event
        self.pitch_class_mask = [1 if item == "YES" else 0 for item in pitch_class_mask]
        self.octave = octave
        self.bass = bass
        self.bass_octave = bass_octave
        self.meter = meter
        self.chord_label = chord_label

    def __eq__(self, other):
        return (self.pitch_class_mask == other.pitch_class_mask) and \
               (self.octave == other.octave) and (self.bass == other.bass) and \
               (self.bass_octave == other.bass_octave) and (self.chord_label == other.chord_label)

    def __hash__(self):
        return hash(hash(str(self.pitch_class_mask)) + hash(self.chord_label) + \
               hash(self.bass) + hash(self.meter))

    def get_chord(self, notes_freq):
        # 12 - length of octave
        # 2-4 working octaves
        return [notes_freq[(self.octave-2)*12 + i] if self.pitch_class_mask[i] else 0 for i in range(0, 12)]

    def get_bass(self, notes_freq):
        # ДОДЕЛАЙЁ
        # return notes_freq[self.bass_octave * 12 + self.bass]
        pass
