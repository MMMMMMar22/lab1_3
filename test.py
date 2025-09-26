def test_count_common_elements():
    # Тестирование функции count_common_elements
    # Тест 1: Обычные списки с общими элементами
    
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 5]
    list3 = [3, 4, 5, 6]
    result = count_common_elements(list1, list2, list3)
    print(f"Тест 1: {result} общих элементов (ожидается 2) - {'Пройден' if result == 2 else 'Не пройден'}")
    # Тест 2: Нет общих элементов
    list4 = [1, 2, 3]
    list5 = [4, 5, 6]
    result = count_common_elements(list4, list5)
    print(f"Тест 2: {result} общих элементов (ожидается 0) - {'Пройден' if result == 0 else 'Не пройден'}")
    # Тест 3: Все элементы общие
    list6 = [1, 2, 3]
    list7 = [1, 2, 3]
    result = count_common_elements(list6, list7)
    print(f"Тест 3: {result} общих элементов (ожидается 3) - {'Пройден' if result == 3 else 'Не пройден'}")
    # Тест 4: Пустые списки
    list8 = []
    list9 = [1, 2, 3]
    result = count_common_elements(list8, list9)
    print(f"Тест 4: {result} общих элементов (ожидается 0) - {'Пройден' if result == 0 else 'Не пройден'}")
    # Тест 5: Один список
    list10 = [1, 2, 3]
    result = count_common_elements(list10)
    print(f"Тест 5: {result} общих элементов (ожидается 3) - {'Пройден' if result == 3 else 'Не пройден'}")
    # Тест 6: Три списка с одним общим элементом
    list11 = [1, 2, 3]
    list12 = [2, 4, 5]
    list13 = [2, 6, 7]
    result = count_common_elements(list11, list12, list13)
    print(f"Тест 6: {result} общих элементов (ожидается 1) - {'Пройден' if result == 1 else 'Не пройден'}")


test_count_common_elements()
print("\nТестирование завершено!")
