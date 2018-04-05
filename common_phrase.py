# return the most common word within this string
from collections import defaultdict


def find_most_common(phrase):
    """Return the most commonly word used in given phrase.

    >>> find_most_common('I really like my friend of a friend')
    ['friend']

    """
    word_counts = defaultdict(int)

    words = phrase.split(' ')

    largest_count = 0
    common_words = []

    for word in words:
        word_counts[word] += 1

        if word_counts[word] == largest_count:
            common_words.append(word)
        if word_counts[word] > largest_count:
            common_words = [word]
            largest_count = word_counts[word]

    return common_words
