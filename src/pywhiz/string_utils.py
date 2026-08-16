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


def odd_count(num):
    """Counts of odd  numbers"""
    count=0
    for i in num:
        if isinstance(i,str) and i.isdigit():
            i=int(i)
        if isinstance(i,int) and i%2!=0:
            count+=1
    return count

def even_count(num):
    """Counts of even  numbers"""
    count=0
    for i in num:
        if isinstance(i,str) and i.isdigit():
            i=int(i)
        if isinstance(i,int) and i%2==0:
            count+=1
    return count

def countf(obj,file):
    with open(file, 'r') as f:
        n=0
        for line in f:
            words = line.split()
            for word in words:
                if obj == word:
                    n+=1
    return n

def positionf(word,file):
    with open(file, 'r') as f:
        text = f.readlines()
        for y, line in enumerate(text, start=1):
           for x, w in enumerate(line.split(), start=1):
               if w == word:
                 return (x, y)
       
    return None


