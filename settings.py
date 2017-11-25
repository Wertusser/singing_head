import os


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(DIR_PATH + "/model/static/jsbach_chorals_harmony.data")

# ничего не трогать в NOTES!
NOTES_FREQ = [int((440.0 / 32) * (2 ** ((x - 9) / 12))) for x in range(36, 73)]

PHONEMES = {
    'a': 'aa',
    # 'a': 'ae',
    'u': 'ah',
    'ou': 'ao',
    'o': 'aw',
    # 'a': 'ax',
    # 'i': 'ay',
    'b': 'b',
    'ch': 'ch',
    'd': 'd',
    # 'd': 'dx',
    'th': 'dh',
    'e': 'eh',
    # 'l': 'el',
    # 'a': 'ey',
    'f': 'f',
    'g': 'g',
    'h': 'hx',
    'i': 'ih',
    # 'e': 'iy',
    'j': 'jh',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'ng': 'nx',
    # 'o': 'ow',
    'oy': 'oy',
    'p': 'p',
    'r': 'r',
    'er': 'rr',
    's': 's',
    'sh': 'sh',
    't': 't',
    # 'th': 'th',
    # 'u': 'uh',
    # 'o': 'uw',
    'v': 'v',
    'w': 'w',
    'y': 'yx',
    'z': 'z',
}
