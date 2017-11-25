def text2phonemes(text, phonemes):
    words = text.split(' ')
    new_text = []
    for word in words:
        for lowel_i in range(0, len(word)):
            try:
                if word[lowel_i] + word[lowel_i + 1] in phonemes:
                    new_text.append(
                        phonemes[word[lowel_i] + word[lowel_i + 1]])
                    continue
            except IndexError:
                pass
            if word[lowel_i] in phonemes:
                new_text.append(phonemes[word[lowel_i]])
        new_text.append(' ')
    return new_text[:-1]


def compile_chord_to_text(chord, length, phoneme):
    voices = []
    for freq in chord:
        if freq > 0:
            voices.append(freq)
    compiled_text = ["{phoneme}<{length},{freq}>".format(phoneme=phoneme, freq=freq, length=length) for freq in voices]
    if len(voices) < 4:
        compiled_text.append("{phoneme}<{length}>".format(phoneme="_", length=length))
    return compiled_text


def compile_chords_to_text(chords, length, phonemes):
    compile_parts = []
    for i in range(0, len(phonemes)):
        compile_parts.append(compile_chord_to_text(chords[i], length, phonemes[i]))
    return compile_parts


def compile(chords, length, phonemes, voices):
    # ВСЕГО 4 ГОЛОСА!!
    data = compile_chords_to_text(chords, length, phonemes)
    texts = []
    for i in range(0, voices):
        text = "[:phoneme on]["
        for data_part in data:
            text += data_part[i]
        texts.append(text+"]")
    return texts
