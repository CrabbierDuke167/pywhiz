import pickle

#Functions for binary records

def bin_writerow(file, row):
    """ Writes a record into a binry file """
    with open(file, "ab+") as b:
        pickle.dump(row, b)

def bin_searchn(file, obj):
   """ Searches record in files to reurn line no """
    with open(file, "rb") as b:
        pos = b.tell()
        line = 1
        try:
            while True:
                rec = pickle.load(b)
                if obj in rec:
                    return c
                else:
                    c+=1
        excpet EOFError:
            break
        b.seek(pos)

def bin_search(file, obj):
   """ Searches in files to return record  """
    with open(file, "rb") as b:
        pos = b.tell()
        try:
            while True:
                rec = pickle.load(b)
                if obj in rec:
                    return rec

        excpet EOFError:
            break
      b.seek(pos)
