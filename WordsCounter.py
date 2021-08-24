import urllib.request


def count_words_in_text(txt: str, counts=None):
    if counts is None:
        counts = dict()
    for word in txt.split():
        word = word.strip()
        if word:  # avoid empty words
            word = word.lower()  # assuming case insensitive
            counts[word] = counts.get(word, 0) + 1
    return counts


def count_words_in_file(file_path):
    """
    since that file can be large, we want to read it in chunks - so the memory will not overflow
    we don't have info regarding lines (if there are lines or it is a big one line, so not using lines iterator
    last word in each chunk will be appended to next chunk to avoid splitting words
    """
    counts = dict()
    buffer = ''
    with open(file_path, 'r') as f:
        cur_buffer = f.read(1024)
        while cur_buffer:
            latest_word_index = cur_buffer.rfind(' ')
            buffer += cur_buffer[:latest_word_index]
            count_words_in_text(buffer, counts)
            buffer = cur_buffer[latest_word_index + 1:]
            cur_buffer = f.read(1024)
        count_words_in_text(buffer, counts)  # check latest word
    return counts


def count_words_in_url(url):
    response = urllib.request.urlopen(url)
    txt = response.read().decode(response.headers.get_content_charset())
    return count_words_in_text(txt)

# words = count_words_in_text("")
# count_words_in_text("hello world", words)
# print('hello w'.rfind(' '))
# print('hello w'[:5])
# print('hello w'[6:])
# print(words)
# print(count_words_in_file('alice29.txt'))
# print(count_words_in_url(
#     'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt'))
