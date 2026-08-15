import string


def v_count(text):
    """Counts vowels."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count+=1
    return count

def c_count(text):
    """Counts consonants."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count+=1

    return count

def w_count(text):
    """Returns word count."""
    words = text.split()
    return(len(words))