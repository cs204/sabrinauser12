var = input('Приветствие: ')

if var.startswith('здравствуйте'):
    print('$0')
elif var[0] == 'з' and var.startswith('здравствуйте') == False:
    print('$20')
else:
    print('$100')