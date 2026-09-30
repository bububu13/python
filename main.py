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


print()
def sequence():
    f = open('sequence.txt')
    s = [float(j) for j in f ]
    positive = []
    negative = []
    for i in s[:]:
        if i<0:
            negative.append(i)
        else:
            positive.append(i)

    print(f'{BLUE}{' '*int(len(negative)/5)}{(len(negative)/(len(positive)+len(negative)))*100}%{RESET}'+'Отрицательные')
    print(f'{RED}{' ' * int(len(positive) / 5)}{(len(positive) / (len(positive) + len(negative))) * 100}%{RESET}'+'Положительные')
sequence()
