from .objects import Chord
import pickle


def get_data(path):
    with open(path, "r") as file:
        return file.readlines()


def format_data(raw_data):
    return [line.strip().replace(' ', '').split(',') for line in raw_data]


def data_to_objects(data, octave, bass_octave):
    chords = []
    for item in data:
        chord = Chord(choral_id=item[0], event=item[1], pitch_class_mask=[i for i in item[2:14]],
                      octave=octave, bass=item[14], bass_octave=bass_octave, meter=item[15], chord_label=item[16])
        chords.append(chord)
    return chords


def get_pairs(chords):
    return list(zip(chords[:], chords[1:]))


def compare_data(pairs):
    data = []
    len_pairs = len(pairs)
    for pair in set(pairs):
        frame = {}
        count = 0
        for item in pairs:
            if pair == item:
                count += 1
        frame["pair"] = pair
        frame["index"] = (count / len_pairs) * 100
        data.append(frame)
    return data


def save_data_to_pkl(data, name):
    with open('{}.pickle'.format(name), 'wb') as f:
        pickle.dump(data, f)


def get_data_from_pkl(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def get_freq(chords, notes_freq):
    return [chord.get_chord(notes_freq=notes_freq) for chord in chords]