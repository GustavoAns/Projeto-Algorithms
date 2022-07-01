def is_palindrome_recursive(word, low_index, high_index):
    try:
        if low_index == high_index:
            return True
        if high_index - low_index == 1 and word[low_index] == word[high_index]:
            return True
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return False
    except IndexError:
        return False