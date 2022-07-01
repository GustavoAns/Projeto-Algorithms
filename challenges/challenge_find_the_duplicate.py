from collections import Counter


def find_duplicate(nums):
    try:
        most_common = Counter(nums).most_common(1)[0]
        if type(most_common[0]) is str or most_common[0] < 0:
            return False
        if most_common[1] > 1:
            return most_common[0]
        return False
    except IndexError or ValueError:
        return False
