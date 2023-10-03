def convert(string):
    string = string.replace(':)', '🙂').replace(':(', '🙁')
    return string

def main():
    user_input = input()
    result = convert(user_input)
    print(result)

if __name__ == "__main__":
    main()