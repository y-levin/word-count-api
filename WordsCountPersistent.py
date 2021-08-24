import pickledb

# using pickledb as simple key-value store
db = pickledb.load('wordsCount.db', False)


def persist_counts(counts: dict):
    for word, count in counts.items():
        if db.exists(word):
            db.append(word, count)  # append adds the new value to the existing value (+=)
        else:
            db.set(word, count)
    db.dump()


def get_word_statistics(word: str):
    word = word.lower()
    if db.exists(word):  # assuming case insensitive
        return db.get(word)
    return 0
