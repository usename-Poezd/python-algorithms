arrUnsorted = [x for x in range(10**3, 0, -1)]


def bubble_sort(arr):
    """
    Алгоритм пробегается по списку и сравнивает соседние элементы
    :param arr: список, который мы хотим отсортировать
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    pass


bubble_sort(arrUnsorted)
print(arrUnsorted)
