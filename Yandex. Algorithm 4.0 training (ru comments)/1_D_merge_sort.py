# D. Сортировка слиянием
#
# Ограничение времени: 15 секунд
# Ограничение памяти: 512 Mb
#
# Ввод: стандартный ввод или input.txt.txt
# Вывод: стандартный вывод или output.txt
#
# Реализуйте сортировку слиянием, используя алгоритм из предыдущей задачи.
#
# На каждом шаге делите массив на две части, сортируйте их независимо и сливайте с помощью уже реализованной функции.
#
# Формат ввода:
# В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 106).
# Во второй строке содержатся N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).
#
# Формат вывода:
# Выведите результат сортировки, то есть N целых чисел, разделенных пробелами, в порядке неубывания.
#
# Пример 1
# Ввод:
# 5
# 1 5 2 4 3
# Вывод:
# 1 2 3 4 5
#
# Примечания:
# Используйте функцию, реализованную в предыдущей задаче.

def merge_sort(sorting_list):
    if len(sorting_list) < 2:
        return sorting_list
    elif len(sorting_list) == 2:
        if sorting_list[0] > sorting_list[1]:
            return [sorting_list[1], sorting_list[0]]
        else:
            return sorting_list
    left = merge_sort(sorting_list[:len(sorting_list) // 2])
    right = merge_sort(sorting_list[len(sorting_list) // 2:])
    li, ri = 0, 0
    result = []
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        elif right[ri] < left[li]:
            result.append(right[ri])
            ri += 1
        else:
            result.append(left[li])
            result.append(right[ri])
            li += 1
            ri += 1
    while li < len(left):
        result.append(left[li])
        li += 1
    while ri < len(right):
        result.append(right[ri])
        ri += 1
    return result


b_n = int(input())
b = list(map(int, input().split()))  # здесь аналогично

res = merge_sort(b)

res_str = " ".join(map(str, res))  # тут тоже join и map позволяют вытащить пару секунд
print(res_str)
