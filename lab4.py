

items = {'r': (3,25),
        'p': (2,15),
        'a': (2,15),
        'm': (2,20),
        'i': (1,5),
        'k': (1,15),
        'x': (3,20),
        't': (1,25),
        'f': (1,15),
        's': (2,20),
        'c': (2,20)}

def get_weight_and_value(items):
    weight = [items[item][0] for item in items]
    value = [items[item][1] for item in items]
    return weight, value

def get_memtable(items, A=7):
    weight, value = get_weight_and_value(items)
    n = len(value)
    V = [[0 for a in range(A+1)] for i in range(n+1)]
    for i in range(n+1):
        for a in range(A+1):
            if i == 0 or a==0:
                V[i][a] = 0


            elif weight[i-1] <=a:
                V[i][a] = max(value[i-1]+ V[i-1][a-weight[i-1]], V[i-1][a])
            else:
                V[i][a] = V[i-1][a]
    return V, weight, value


def get_selected_items_list(items, A=7):
    V, weight, value = get_memtable(items, A)
    n = len(value)
    items_keys = list(items.keys())

    selected_items = []
    a = A
    for i in range(n, 0, -1):
        if V[i][a] != V[i - 1][a]:
            selected_items.append(items_keys[i - 1])
            a -= weight[i - 1]

    return selected_items

stuff = get_selected_items_list(items)
stuff.append('d')

points = sum([items[j][1]*2 for j in stuff])-sum([items[j][1] for j in items])

#матрица
rows=2
cols = 4
chosen = {}
for i in stuff:
    chosen[i] = items[i][0]

cells = []
for item, size in chosen.items():
    cells.extend([item]*size)


matrix = [cells[r * cols: (r + 1) * cols] for r in range(rows)]

for row in matrix:
    print(','.join(f'[{cell}]' for cell in row))

print('Очков выживания:', points)