# Given list of words, return a list of lists where each list contains words
# that are anagrams of each other.
from collections import defaultdict


def find_anagrams(words):
    """Returns lists of words that are anagrams of each other.

    >>> find_anagrams(['bus', 'sub', 'pythonic', 'hypnotic', 'sbu', 'bird'])
    [['bus', 'sub', 'sbu'], ['pythonic', 'hypnotic']]

    """

    anagram_groups = []

    anagrams = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    for anagrams in anagrams.values():
        if len(anagrams) > 1:
            anagram_groups.append(anagrams)

    return anagram_groups


find_anagrams(['bus', 'sub', 'pythonic', 'hypnotic'])
