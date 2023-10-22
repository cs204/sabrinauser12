file_name = input('File name: ')
file_extension = file_name.split('.')[-1].lower()

if file_extension in ['gif', 'jpg', 'jpeg', 'png']:
    if file_extension == 'jpg':
        print('image/jpeg')
    else:
        print(f'image/{file_extension}')
elif file_extension in ['pdf', 'zip']:
    print(f'application/{file_extension}')
elif file_extension == 'txt':
    print('text/plain')
else:
    print('application/octet-stream')