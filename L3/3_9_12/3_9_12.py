def mask_card(digits: str) -> str:
    return f"**** **** **** {digits[-4:]}"


raw = input("Введіть 16 цифр картки: ").replace(" ", "")
if len(raw) == 16 and raw.isdigit():
    print(mask_card(raw))
else:
    print("Помилка: потрібно рівно 16 цифр.")