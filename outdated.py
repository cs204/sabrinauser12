import re

def convert_to_iso_format(date_str):
    months = {
        "январь": "01",
        "февраль": "02",
        "март": "03",
        "апрель": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "август": "08",
        "сентябрь": "09",
        "октябрь": "10",
        "ноябрь": "11",
        "декабрь": "12"
    }

    date_match = re.search(r"(\d{1,2})[.\s](\d{1,2}|[а-я]+)[.\s](\d{4})", date_str)
    if date_match:
        day, month, year = map(str, date_match.groups())

        if month.isdigit():
            month_num = int(month)
            if 1 <= month_num <= 12 and 1 <= int(day) <= 31:
                return f"{year}-{month_num:02d}-{int(day):02d}"
        else:
            month_str = months.get(month.lower())
            if month_str and 1 <= int(day) <= 31:
                return f"{year}-{month_str}-{int(day):02d}"

    return None

def outdated_program():
    while True:
        date_input = input("Дата: ")
        iso_date = convert_to_iso_format(date_input)
        if iso_date:
            print(iso_date)
            break

if __name__ == "__main__":
    outdated_program()