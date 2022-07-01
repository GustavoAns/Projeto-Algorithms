# Course dia 36.3 Algoritmos de ordenação e Busca
# Algoritmos que usam dividir e conquistar / Merge Sort
def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


# função auxiliar que realiza a mistura dos dois arrays
def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


# Escolha Merge , Pior caso = O(n log n)
def is_anagram(first_string, second_string):
    try:
        if not first_string or not second_string:
            return False
        if len(first_string) != len(second_string):
            return False
        first_list = list(first_string.lower())
        second_list = list(second_string.lower())
        merge_sort(first_list)
        merge_sort(second_list)
        return first_list == second_list
    except TypeError:
        return False
