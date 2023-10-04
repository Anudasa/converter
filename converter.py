def binary_to_denery(num):
    num = str(num)
    denery = 0
    for i in range(len(num)):
        index = -(i + 1)
        digit = 2**i * int(num[index])
        denery += digit
    return denery

def hexedecimal_to_denery(num):
    hexedecimal_system = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,}
    num_new = []
    denery = 0
    
    num = num.upper()

    for i in num:
        digit = hexedecimal_system[i]
        num_new.append(digit)

    for i in range(len(num_new)):
        index = -(i + 1)
        digit = (16**i) * num_new[index]
        denery += digit
    return denery

def denery_to_binary(num):
    binary = ""
    num = int(num)
    
    while num > 0:
        reminder = num % 2
        binary = str(reminder) + binary
        num = num // 2
    return binary

def denery_to_hexedecimal(num):
    hexedecimal_system = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexedecimal = ""
    num = int(num)

    while int(num) > 0:
        reminder = num % 16
        if reminder >= 10:
            reminder = hexedecimal_system[reminder]
        hexedecimal = str(reminder) + hexedecimal
        num = num // 16
    return hexedecimal

def prosses(answer):
    initial_systems = {'binary': binary_to_denery, 'hex': hexedecimal_to_denery}
    disered_systems = {'binary': denery_to_binary, 'hex': denery_to_hexedecimal}
    global denery

    answer = answer.split()

    if answer[0] == answer[2]:
        print(answer[1])
        return 0

    for i in initial_systems:
        if answer[0] == "denery":
            denery = answer[1]
            break
        elif answer[0] == i:
            denery = initial_systems[i](answer[1])
            break
        else:
            print("Такой системы счисления не существует 1")
            return 0

    for i in disered_systems:
        if answer[2] == 'denery':
            print(denery)
            break
        elif answer[2] == i:
            print(disered_systems[i](denery))
            break
        else:
            print("Такой системы счисления не существует 2")
            break


print("Enter using only space bar without any other symbols: initial_system number disered_system")
answer = input()
prosses(answer)
