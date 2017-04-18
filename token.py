def spell_check(vocabulary_file, text_file, special_characters=[",", ".", "'", ";", "\n"]):
    misspelled_words = []

    f = open(vocabulary_file).read()
    g = open(text_file).read()

    tokenized_vocabulary = tokenize(g, special_characters)
    tokenized_text = tokenize(f, special_characters, True)

    for token in tokenized_text:
        if token not in tokenized_vocabulary and token != "":
            misspelled_words.append(token)
    return (misspelled_words)


final_mispelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")

print(final_mispelled_words)


def spell_check(vocabulary_file, text_file, special_characters=[",", ".", "'", ";", "\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()

    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return (misspelled_words)


final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)