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

