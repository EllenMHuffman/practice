# Given a block of text and an array of key words, return the count of the
# occurence of phrase in text


def count_phrase(text, phrase):
    """Given text and array phrase, return count of array phrase in text.

    >>> count_phrase('the cow jumped over the moon the moon', ['the', 'moon'])
    2

    """

    text = text.split(' ')
    count = 0
    # import pdb; pdb.set_trace()
    for i, word in enumerate(text):
        if word == phrase[0]:
            if text[i: i + len(phrase)] == phrase:
                count += 1

    return count
