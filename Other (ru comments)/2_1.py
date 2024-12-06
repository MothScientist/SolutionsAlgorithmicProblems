# Клумбы 2.0
# Как предыдущая задача, но соседние клумбы могут сливаться в одну

# Примеры:
# 1)
# Ввод:
# 5
# 2 3
# 5 6
# 7 10
# 1 2
# 3 4
# Вывод:
# 1 10

# 2)
# Ввод:
# 5
# 2 3
# 5 6
# 3 4
# 3 4
# 8 10
# Вывод:
# 2 6
# 8 10

# 3)
# Ввод:
# 3
# 2 3
# 5 10
# 3 5
# Вывод:
# 2 10
#
# Решение:

def flowers(arr, seats):
    for _ in range(len(arr)):
        for i in arr:
            if i[0] <= seats[0] <= i[1] <= seats[1]:  # Нижняя граница добавляется
                seats[0] = i[0]
                for _ in range(arr.count(i)):
                    arr.remove(i)
            elif i[1] >= seats[1] >= i[0] >= seats[0]:  # Верхняя граница добавляется
                seats[1] = i[1]
                for _ in range(arr.count(i)):
                    arr.remove(i)
            elif i[0] <= seats[0] and i[1] >= seats[1]:  # Старый массив полностью входит в новые рамки
                seats[0] = i[0]
                seats[1] = i[1]
                for _ in range(arr.count(i)):
                    arr.remove(i)
            elif i[1] + 1 == seats[0]:  # Новый массив примыкает слева
                seats[0] = i[0]
                for _ in range(arr.count(i)):
                    arr.remove(i)
            elif i[0] - 1 == seats[1]:  # Новый массив примыкает справа
                seats[1] = i[1]
                for _ in range(arr.count(i)):
                    arr.remove(i)
    print(seats)
    for i in arr:
        print(i)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
flowers(a, a[0])
