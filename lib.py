def count_common_elements(*lists):
    if not lists:
        return 0
    
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements = common_elements.intersection(set(lst))
    
    return len(common_elements)

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]
list3 = [3, 4, 5, 6]
    
result = count_common_elements(list1, list2, list3)
print(f"Количество общих элементов: {result}")
