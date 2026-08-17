
def txt_wc(obj,file):
    """Count number of a string/word"""
    with open(file, 'r') as f:
        n=0
        for line in f:
            words = line.split()
            for word in words:
                if obj == word:
                    n+=1
    return n

def txt_w_pos(word,file):
    """Return position(line,nth word) of word"""
    with open(file, 'r') as f:
        text = f.readlines()
        for y, line in enumerate(text, start=1):
           for x, w in enumerate(line.split(), start=1):
               if w == word:
                 return (x, y)
       
    return None

def txt_cc(obj):
    """Count number of characters"""
    with open(obj, 'r') as f:
        text = f.read()
        n = 0
        for char in text:
            n+=1
    return n

def txt_lc(obj):
    """Count number of lines"""
    with open(obj, "r") as f:
        lines = f.readlines()
        n = len(lines)
    return n