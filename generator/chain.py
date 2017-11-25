import random


def get_similar_pair(frame, data):
    last_chord = frame["pair"][1]
    similar_chords = []
    for item in data:
        if last_chord == item["pair"][1] and frame["pair"] != item["pair"]:
            similar_chords.append(item)
    return similar_chords


def get_next_random(frame, data, min_p=0):
    similar_chords = get_similar_pair(frame, data)
    normalized_chords = []
    for chord in similar_chords:
        if chord["index"] > min_p:
            normalized_chords.append(chord)
    return random.choice(normalized_chords) if normalized_chords != [] else frame


def get_next_max(frame, data):
    similar_chords = get_similar_pair(frame, data)
    max_index = 0
    max_chord = None
    for chord in similar_chords:
        if chord['index'] > max_index:
            max_index = chord['index']
            max_chord = chord
    return max_chord if max_chord else frame


def get_next_min(frame, data):
    similar_chords = get_similar_pair(frame, data)
    min_index = 1
    min_chord = None
    for chord in similar_chords:
        if chord['index'] < min_index:
            min_index = chord['index']
            min_chord = chord
    return min_chord if min_chord else frame


def get_chain(length):
    return [random.choice(['R', '>', '<']) for _ in range(0, length)]


def generate(length, data, min_p=0, frame=None, chain=None):
    chords = []
    next_frame = random.choice(data)
    generated_chain = get_chain((length))
    if frame:
        next_frame = frame
    if chain:
        generated_chain = chain
    print("".join(generated_chain))
    for step in generated_chain:
        chords.append(next_frame['pair'])
        if step == "R":
            next_frame = get_next_random(next_frame, data, min_p)
        if step == ">":
            next_frame = get_next_max(next_frame, data)
        if step == "<":
            next_frame = get_next_min(next_frame, data)
    # Изменить, а то чето непонятно!
    return list(list(zip(*chords))[0]) + [chords[-1][-1]]
