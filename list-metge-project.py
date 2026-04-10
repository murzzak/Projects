def input_list():
    a = input("Введите числа через пробел: ")
    parts = a.split()
    result = []

    for i in parts:
        if i.isdigit():
            result.append(int(i))
        else:
            print("Обнаружено не число, пропускаем:", i)

    return result


def merge_lists(a, b):
    return a + b


def merge_unique(a, b):
    result = []
    for i in a + b:
        if i not in result:
            result.append(i)
    return result


def merge_sorted(a, b):
    result = a + b
    result.sort()
    return result


while True:
    print("\n1 - объединить списки")
    print("2 - без повторов")
    print("3 - сортировать")
    print("4 - выход")

    choice = input("Выбор: ")

    if choice == "4":
        print("Программа завершена")
        break

    if choice != "1" and choice != "2" and choice != "3":
        print("Неверный ввод\n")
        continue

    print("\nПервый список:")
    list1 = input_list()

    print("\nВторой список:")
    list2 = input_list()

    if choice == "1":
        res = merge_lists(list1, list2)
    elif choice == "2":
        res = merge_unique(list1, list2)
    else:
        res = merge_sorted(list1, list2)

    print("\nРезультат:", res)
