# Task 18. Найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 20, 30, 42, 50]
k = int(input("Введите число, которое надо проверить: "))
t = k
near = list_1[0]
for i in range(1, len(list_1)):
    if list_1[i] == k:
        near = k
        t = 0
    else:
        d = k - list_1[i]
        if d < 0:
            d *= -1
        if d < t:
            t = d
            near = list_1[i]    
print(f"Самый близкий по величине элемент: {near}")

