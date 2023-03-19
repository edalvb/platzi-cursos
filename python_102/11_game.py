import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')

    user_opt = input("Piedra, papel o tijera =>").lower()

    if user_opt not in options:
        print("Opción no válida")
        return choose_options()

    computer_opt = random.choice(options)

    print("Tu opción: ", user_opt)
    print("Opción del computador: ", computer_opt)

    return user_opt, computer_opt


def check_rules(u_win, c_win, user_option, computer_option):
    if user_option == computer_option:
        print("Empate!")
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print("Ganaste!")
            u_win += 1
        else:
            print("Perdiste!")
            c_win += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print("Ganaste!")
            u_win += 1
        else:
            print("Perdiste!")
            c_win += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print("Ganaste!")
            u_win += 1
        else:
            print("Perdiste!")
            c_win += 1

    return u_win, c_win


def run_game():
    rounds = 0
    user_win = 0
    computer_win = 0

    while True:
        print('*' * 10)
        print("Ronda ", rounds)
        print('*' * 10)

        print('Tú: ', user_win, ' - Computador: ', computer_win)

        user_option, computer_option = choose_options()

        user_win, computer_win = check_rules(
            user_win,
            computer_win,
            user_option,
            computer_option
        )

        if computer_win == 2:
            print("Perdiste el juego!")
            break
        elif user_win == 2:
            print("Ganaste el juego!")
            break

        rounds += 1


run_game()
