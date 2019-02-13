import os



class InkColor:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    FLASHING = '\033[5m'
    INVERT = '\033[7m'
    LIGHTCYAN = '\033[96m'
    CYAN = '\033[36m'
    BLACK = '\033[97m'
    LIGHTGREY = '\033[37m'
    GRAY = '\033[90m'
    DARKGRAY = '\033[30m'
    RED = '\033[31m'
    LIGHTRED = '\033[91m'
    GREEN = '\033[32m'
    LIGHTGREEN = '\033[92m'
    BLUE = '\033[34m'
    LIGHTBLUE = '\033[94m'
    PURPLE = '\033[35m'
    LIGHTPURPLE = '\033[95m'
    LIGHTYELLOW = '\033[93m'
    YELLOW = '\033[33m'
    BG_GRAY = '\033[40m'
    BG_BLACK = '\033[100m'
    BG_RED = '\033[41m'
    BG_LIGHTRED = '\033[101m'
    BG_BLUE = '\033[44m'
    BG_LIGHTBLUE = '\033[104m'
    BG_PURPLE = '\033[45m'
    BG_LIGHTPURPLE = '\033[105m'
    BG_LIGHTYELLOW = '\033[43m'
    BG_YELLOW = '\033[103m'
    BG_GREEN = '\033[42m'
    BG_LIGHTGREEN = '\033[102m'
    BG_LIGHTCYAN = '\033[46m'
    BG_CYAN = '\033[106m'


class ink:
    # '\033[0m'
    ENDC = InkColor.ENDC
    # '\033[1m'
    BOLD = InkColor.BOLD
    # '\033[2m'
    DIM = InkColor.DIM
    # '\033[4m'
    UNDERLINE = InkColor.UNDERLINE
    # '\033[5m'
    FLASHING = InkColor.FLASHING
    # '\033[96m'
    LIGHTCYAN = InkColor.LIGHTCYAN
    # '\033[36m'
    CYAN = InkColor.CYAN
    # '\033[97m'
    BLACK = InkColor.BLACK
    # '\033[37m'
    LIGHTGREY = InkColor.LIGHTGREY
    # '\033[90m'
    GRAY = InkColor.GRAY
    # '\033[30m'
    DARKGRAY = InkColor.DARKGRAY
    # '\033[31m'
    RED = InkColor.RED
    # '\033[91m'
    LIGHTRED = InkColor.LIGHTRED
    # '\033[32m'
    GREEN = InkColor.GREEN
    # '\033[92m'
    LIGHTGREEN = InkColor.LIGHTGREEN
    # '\033[34m'
    BLUE = InkColor.BLUE
    # '\033[94m'
    LIGHTBLUE = InkColor.LIGHTBLUE
    # '\033[35m'
    PURPLE = InkColor.PURPLE
    # '\033[95m'
    LIGHTPURPLE = InkColor.LIGHTPURPLE
    # '\033[93m'
    LIGHTYELLOW = InkColor.LIGHTYELLOW
    # '\033[33m'
    YELLOW = InkColor.YELLOW
    # '\033[40m'
    BG_GRAY = InkColor.BG_GRAY
    # '\033[100m'
    BG_BLACK = InkColor.BG_BLACK
    # '\033[41m'
    BG_RED = InkColor.BG_RED
    # '\033[101m'
    BG_LIGHTRED = InkColor.BG_LIGHTRED
    # '\033[44m'
    BG_BLUE = InkColor.BG_BLUE
    # '\033[104m'
    BG_LIGHTBLUE = InkColor.BG_LIGHTBLUE
    # '\033[45m'
    BG_PURPLE = InkColor.BG_PURPLE
    # '\033[105m'
    BG_LIGHTPURPLE = InkColor.BG_LIGHTPURPLE
    # '\033[43m'
    BG_LIGHTYELLOW = InkColor.BG_LIGHTYELLOW
    # '\033[103m'
    BG_YELLOW = InkColor.BG_YELLOW
    # '\033[42m'
    BG_GREEN = InkColor.BG_GREEN
    # '\033[102m'
    BG_LIGHTGREEN = InkColor.BG_LIGHTGREEN
    # '\033[46m'
    BG_LIGHTCYAN = InkColor.BG_LIGHTCYAN
    # '\033[106m'
    BG_CYAN = InkColor.BG_CYAN


    @classmethod
    def pl(cls, print_var, color_1: InkColor, color_2: InkColor, _e=""):
        """
                ink.pl('this text is blue and bold.', ink.BLUE, ink.BOLD, "\n")
        """
        print(color_1, end="")
        print(color_2, end="")
        print(print_var, end=_e)
        print(cls.ENDC, end="")
        print(cls.ENDC, end="")

    @classmethod
    def p(cls, print_var, color: InkColor, _e=""):
        """
        ink.p('this text is red.', ink.RED, "\n")
        """
        print(color, end="")
        print(print_var, end=_e)
        print(cls.ENDC, end="")



    @classmethod
    def help_examples(cls):

        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


        LIGHTCYAN = '\033[96m'
        CYAN = '\033[36m'

        BLACK = '\033[97m'
        LIGHTGREY = '\033[37m'

        GRAY = '\033[90m'
        BLACK = '\033[30m'

        RED = '\033[31m'
        LIGHTRED = '\033[91m'

        GREEN = '\033[32m'
        LIGHTGREEN = '\033[92m'

        BLUE = '\033[34m'
        LIGHTBLUE = '\033[94m'

        PURPLE = '\033[35m'
        LIGHTPURPLE = '\033[95m'

        LIGHTYELLOW = '\033[93m'
        YELLOW = '\033[33m'

        BG_GRAY = '\033[40m'
        BG_BLACK = '\033[100m'

        BG_RED = '\033[41m'
        BG_LIGHTRED = '\033[101m'

        BG_BLUE = '\033[44m'
        BG_LIGHTBLUE = '\033[104m'

        BG_PURPLE = '\033[45m'
        BG_LIGHTPURPLE = '\033[105m'

        BG_LIGHTYELLOW = '\033[43m'
        BG_YELLOW = '\033[103m'

        BG_GREEN = '\033[42m'
        BG_LIGHTGREEN = '\033[102m'

        BG_LIGHTCYAN = '\033[46m'
        BG_CYAN = '\033[106m'



    @classmethod
    def print_everything_possible(cls):
        os.system("clear")
        this_ink = '\033[91m'
        i = 0
        while i < 150:
            if i < 108 and i > 89:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            elif i < 48 and i > 30:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            elif i < 48 and i > 30:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            elif i > 0 and i < 9:
                print(cls.ENDC, end=" \033[" + str(i) + "m ◀█  \\033[" + str(i) + "m  █▶☀ ︎✏︎ ✈ ︎♚ ♛ ♜ ♝ ♞")
                print(' ♠ ︎♣ ︎♥ ︎♦ ︎● ◎ ■ ❖ ◆ ▶ ︎► ◀ ︎✣ ✢ ✤ ✶ ✱ ✿ ✖ ︎✔ ︎✱ ✮ ◢ ◣ ◢ ◤ ◥ ◤', end="" + cls.ENDC)
                print("\033[" + str(i+1) + "m", end='')
                print()
            i += 1

