user_option = input("Piedra, papel o tijera =>")
computer_option = 'piedra'

if user_option == computer_option:
    print("Empate!")
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print("Ganaste!")
    else:
        print("Perdiste!")
elif user_option == 'papel':
    if computer_option == 'piedra':
        print("Ganaste!")
    else:
        print("Perdiste!")
elif user_option == 'tijera':
    if computer_option == 'papel':
        print("Ganaste!")
    else:
        print("Perdiste!")
