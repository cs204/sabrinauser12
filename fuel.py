def calculate_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        percentage = round(x / y * 100)

        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"

    except (ValueError, ZeroDivisionError):
        return None

def fuel_program():
    while True:
        fraction_input = input("Дробь: ")
        result = calculate_percentage(fraction_input)

        if result is not None:
            print(result)
            break

if __name__ == "__main__":
    fuel_program()