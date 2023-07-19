from actions import welcome_screen, show, find, add, edit, delete


def main():
    welcome_screen()
    while True:
        input_str = input('Your command > ')
        command = input_str.upper()
        match command:
            case 'S':
                show()
            case 'F':
                find()
            case 'A':
                add()
            case 'E':
                edit()
            case 'D':
                delete()
            case 'Q':
                print('Bye!')
                break
            case _:
                print(f"{command}: command not found")


if __name__ == '__main__':
    main()
