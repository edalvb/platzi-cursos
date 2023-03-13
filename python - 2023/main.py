import random

options = ('piedra', 'papel', 'tijera')
rounds = 0
user_win = 0
computer_win = 0

while True:
    print('*' * 10)
    print("Ronda ", rounds)
    print('*' * 10)

    print('Tú: ', user_win, ' - Computador: ', computer_win)

    user_option = input("Piedra, papel o tijera =>").lower()

    if user_option not in options:
        print("Opción no válida")
        continue

    computer_option = random.choice(options)

    print("Tu opción: ", user_option)
    print("Opción del computador: ", computer_option)

    if user_option == computer_option:
        print("Empate!")
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print("Ganaste!")
            user_win += 1
        else:
            print("Perdiste!")
            computer_win += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print("Ganaste!")
            user_win += 1
        else:
            print("Perdiste!")
            computer_win += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print("Ganaste!")
            user_win += 1
        else:
            print("Perdiste!")
            computer_win += 1

    if computer_win == 2:
        print("Perdiste el juego!")
        break
    elif user_win == 2:
        print("Ganaste el juego!")
        break

    rounds += 1
