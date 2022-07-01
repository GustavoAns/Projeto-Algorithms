def is_palindrome_iterative(word):
    try:
        inverted = word[::-1]
        if word == "":
            return False
        if inverted == word:
            return True
        return False
    except TypeError:
        return False
