def print_state(state):
    counter = len(state) - 1

    while counter >= 0:
        line = '|' + '|'.join(state[counter]) + '|'
        print(line)
        counter -= 1


def start():
    sign_empty = '.'
    sign_x = 'X'
    sign_o = 'O'

    state = [
        [sign_empty, sign_empty, sign_empty],
        [sign_empty, sign_empty, sign_empty],
        [sign_empty, sign_empty, sign_empty],
    ]

    print_state(state)

    current_sign = sign_x

    steps = 9
    while steps > 0:
        line_number = int(input('Line: '))
        row_number = int(input('Row: '))

        if state[line_number][row_number] != sign_empty:
            print('Field is not empty')
            continue

        state[line_number][row_number] = current_sign
        current_sign = sign_o

        print_state(state)

        steps -= 1

    print('End game!')


if __name__ == '__main__':
    start()
