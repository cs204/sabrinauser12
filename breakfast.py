menu = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50
}

def calculate_order_cost(order):
    total_cost = 0
    for item in order:
        item_lower = item.lower()
        if item_lower in menu:
            total_cost += menu[item_lower]
    return total_cost

def breakfast_program():
    order = []

    try:
        while True:
            item = input("Блюдо: ")
            order.append(item)
    except EOFError:
        pass

    total_cost = calculate_order_cost(order)
    print(f"\nСумма: {total_cost:.2f}")

if __name__ == "__main__":
    breakfast_program()