def print_messeage(command):
    if command == 'start':
        print('DECOMMENT', '\n')
        print('---------------------------', '\n')
        print("The utility is designed to remove empty lines in code and comments.")
        print("The utility works correctly if the code uses # only in lines and comments.", '\n')
    if command == 'emty':
        print("The 'code.txt' file is empty. Paste the code into this file.", '\n')
        x = input('Enter anything: ') # Заглушка чтобы, консоль не закрывалась
    if command == 'end':
        print('\n')
        print("Success!","\n" "Open the 'new_code.txt' file.")