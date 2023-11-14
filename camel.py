def camel_to_snake(variable_name):
    snake_case = ''
    for char in variable_name:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

def main():
    camel_case_name = input("Верблюжий стиль: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print(snake_case_name)

if __name__ == "__main__":
    main()