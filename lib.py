def count_common_elements(*lists):
    if not lists:
        return 0
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements = common_elements.intersection(set(lst))

    return len(common_elements)

# Тест 1
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
result1 = count_common_elements(list1, list2, list3)
print(f"Тест 1: Общих элементов в 3 списках: {result1}")  # Должно быть 1 (элемент 5)

# Тест 2
list4 = [1, 2, 3]
list5 = [1, 2, 3]
result2 = count_common_elements(list4, list5)
print(f"Тест 2: Общих элементов в 2 одинаковых списках: {result2}")  # Должно быть 3

# Тест 3
list6 = [1, 2, 3]
list7 = [4, 5, 6]
result3 = count_common_elements(list6, list7)
print(f"Тест 3: Общих элементов в разных списках: {result3}")  # Должно быть 0

# Тест 4 - один список
result4 = count_common_elements([1, 2, 3])
print(f"Тест 4: Передан один список: {result4}")  # Должно быть 3

# Тест 5 - пустые списки
result5 = count_common_elements([], [])
print(f"Тест 5: Пустые списки: {result5}")  # Должно быть 0