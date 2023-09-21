# Task 16. Надо вычислить сколько раз встречается число k в массиве list_1

list_1 = [2, 2, 2, 3, 4, 5, 7, 7, 7, 7]
k = int(input("Введите число, которое надо проверить: "))
count = 0
for i in range(0, len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)