RED = '\033[41m'
WHITE = '\033[47m'
BLUE = '\033[44m'
RESET = '\033[0m'
pixel = '   '
lenght = 9
height = 9
for i in range(height):
    if i< height//3:
        print(RED + pixel * lenght + RESET)
    elif height//3<=i<2*height//3:
        print(WHITE + pixel * lenght + RESET)
    else:
        print(BLUE + pixel * lenght + RESET)