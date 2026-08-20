import random


def unique(lst):
    """Removes duplicates while preserving original order."""
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

def duplicates(lst):
    """Returns only the items that appear more than once."""
    seen = []
    dupes = []
    for item in lst:
        if item in seen:
            if item not in dupes:
                dupes.append(item)
        else:
            seen.append(item)
    return dupes

def compact(lst):
    """Removes all falsy values from a list."""
    result = []
    for item in lst:
        if item:
            result.append(item)
    return result

def shuffle(lst):
    """Returns a new shuffled copy of a list."""
    copied = list(lst)
    random.shuffle(copied)
    return copied

def sample(lst, count=1):
    """Picks random items from a list safely."""
    if not lst:
        return []
    k = count
    if k > len(lst):
        k = len(lst)
    return random.sample(lst, k)

def sample_one(lst):
    """Picks a single random item from a list."""
    if not lst:
        return None
    return random.choice(lst)