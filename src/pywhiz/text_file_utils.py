
def count(obj,file):
    with open(file, 'r') as f:
        n=0
        for line in f:
            words = line.split()
            for word in words:
                if obj == word:
                    n+=1
    return n

def position(word,file):
    with open(file, 'r') as f:
        text = f.readlines()
        for y, line in enumerate(text, start=1):
           for x, w in enumerate(line.split(), start=1):
               if w == word:
                 return (x, y)
       
    return None
