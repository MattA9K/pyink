import os

ENDC = '\033[0m'
os.system("clear")

this_ink = '\033[91m'
i = 0
while i < 150:
    if i < 108 and i > 89:
        print(ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
        print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + ENDC)
        print("\033[" + str(i + 1) + "m", end='')
        print()
    elif i < 48 and i > 30:
        print(ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
        print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + ENDC)
        print("\033[" + str(i + 1) + "m", end='')
        print()
    elif i < 48 and i > 30:
        print(ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
        print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + ENDC)
        print("\033[" + str(i + 1) + "m", end='')
        print()
    elif i > 0 and i < 9:
        print(ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
        print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + ENDC)
        print("\033[" + str(i + 1) + "m", end='')
        print()
    i += 1
