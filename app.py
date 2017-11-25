from settings import DIR_PATH, DATA_PATH, NOTES_FREQ, PHONEMES
from model.data import get_data_from_pkl, get_pairs, get_data, format_data, \
    data_to_objects, compare_data, save_data_to_pkl, get_freq
from generator.chain import generate
from synth.compiler import compile, text2phonemes
from synth.save import execute_voice
import time


"""
TODO:
    - исрпавить баг с 4-мя голосами
    - добавить новые голоса
    - оптимизация
    - запаковывать голоса в .wav файл
"""


def prepare_data(octave, bass_octave, filename):
    raw_data = get_data(DATA_PATH)
    data = format_data(raw_data)
    chords = data_to_objects(data, octave, bass_octave)
    pairs = get_pairs(chords)
    model = compare_data(pairs)
    save_data_to_pkl(model, name=filename)


def generate_choir(text, filename, voices, length, attempts=1):
    phonemes = text2phonemes(text, PHONEMES)
    data = get_data_from_pkl("{}.pickle".format(filename))
    for i in range(0, attempts):
        ready = generate(length=len(phonemes), data=data)
        chords = get_freq(ready, NOTES_FREQ)
        choir = compile(chords=chords, length=length, phonemes=phonemes, voices=voices)
        for voice in choir:
            execute_voice(voice, DIR_PATH)
        time.sleep(len(phonemes) * length // 1000 + 1)


if __name__ == '__main__':
    # prepare_data(octave=3, bass_octave=1, filename="test")
    text = """vlaadiimiir puutin molodeetch pooliitik liider i baaetch"""
    generate_choir(text=text, filename="test", voices=3, length=120, attempts=10)
