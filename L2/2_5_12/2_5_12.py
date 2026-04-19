GROUPS: dict = {
    "КС-21": {"count": 24, "headman": "Іваненко О.В."},
    "КС-22": {"count": 22, "headman": "Петренко А.І."},
    "КС-23": {"count": 25, "headman": "Потайчук Р.О."},
    "КС-24": {"count": 20, "headman": "Сидоренко М.К."},
}

while True:
    print("\nМеню:")
    print(" 1. Кількість студентів у групі")
    print(" 2. ПІБ старости групи")
    print(" 3. Кортеж груп, де студентів < заданого значення")
    print(" 4. Кортеж груп, де студентів >= заданого значення")
    print(" 5. Змінити кількість студентів у групі")
    print(" 6. Змінити ПІБ старости групи")
    print(" 7. Додати нову групу")
    print(" 8. Видалити групу")
    print(" 9. Множина ПІБ старост зазначених груп")
    print("10. Вихід")

    choice = input("Оберіть пункт: ").strip()

    if choice == "1":
        g = input("Група: ").strip()
        if g in GROUPS:
            print(f"Кількість студентів у {g}: {GROUPS[g]['count']}")
        else:
            print("Групу не знайдено.")

    elif choice == "2":
        g = input("Група: ").strip()
        if g in GROUPS:
            print(f"Староста {g}: {GROUPS[g]['headman']}")
        else:
            print("Групу не знайдено.")

    elif choice == "3":
        limit = int(input("Максимальна кількість студентів: "))
        result = tuple(g for g, v in GROUPS.items() if v["count"] < limit)
        print(f"Групи з кількістю студентів < {limit}: {result}")

    elif choice == "4":
        limit = int(input("Мінімальна кількість студентів: "))
        result = tuple(g for g, v in GROUPS.items() if v["count"] >= limit)
        print(f"Групи з кількістю студентів >= {limit}: {result}")

    elif choice == "5":
        g = input("Група: ").strip()
        if g in GROUPS:
            GROUPS[g]["count"] = int(input("Нова кількість: "))
            print("Оновлено.")
        else:
            print("Групу не знайдено.")

    elif choice == "6":
        g = input("Група: ").strip()
        if g in GROUPS:
            GROUPS[g]["headman"] = input("Новий ПІБ старости: ").strip()
            print("Оновлено.")
        else:
            print("Групу не знайдено.")

    elif choice == "7":
        g = input("Назва нової групи: ").strip()
        if g in GROUPS:
            print("Група вже існує.")
        else:
            count = int(input("Кількість студентів: "))
            headman = input("ПІБ старости: ").strip()
            GROUPS[g] = {"count": count, "headman": headman}
            print("Додано.")

    elif choice == "8":
        g = input("Група для видалення: ").strip()
        if g in GROUPS:
            del GROUPS[g]
            print("Видалено.")
        else:
            print("Групу не знайдено.")

    elif choice == "9":
        raw = input("Введіть назви груп через пробіл: ").split()
        headmen = {GROUPS[g]["headman"] for g in raw if g in GROUPS}
        not_found = [g for g in raw if g not in GROUPS]
        print(f"Множина ПІБ старост: {headmen}")
        if not_found:
            print(f"Не знайдено: {not_found}")

    elif choice == "10":
        print("Вихід.")
        break

    else:
        print("Невірний пункт меню.")