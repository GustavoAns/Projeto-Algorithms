def is_palindrome_recursive(word, low_i, high_i):
    try:
        if (
            high_i - low_i == 1 and word[low_i] == word[high_i]
        ) or low_i == high_i:
            return True
        if word[low_i] == word[high_i]:
            return is_palindrome_recursive(word, low_i + 1, high_i - 1)
        return False
    except IndexError:
        return False
