def coffee_machine():
    price_per_cup = 50
    amount_due = 0

    while amount_due < price_per_cup:
        print(f"Нужная сумма: {price_per_cup - amount_due}")
        coin = int(input("Вставьте монету: "))
        if coin not in [50, 20, 10, 5]:
            continue
        amount_due += coin

    change_owed = amount_due - price_per_cup
    if change_owed >= 0:
        print(f"Ваша сдача: {change_owed}")

if __name__ == "__main__":
    coffee_machine()