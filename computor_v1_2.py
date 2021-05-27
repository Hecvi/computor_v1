

def checking_for_multiplictaion_signs(ls):
    alpha, sign = 0, 0
    for elem in ls:
        if elem[0].isalpha() and elem not in '+-*':
            alpha += 1
        elif elem == '*':
            sign = 1
        elif alpha > 0 and elem in '+-':
            alpha = 0
    if alpha > 1 and sign == 1:
        exit("Incorrect form of the equation")


def checking_correctness(ls):
    new_ls, tmp_ls = [], []
    for i in range(len(ls)):
        if ls[i].isnumeric() and i > 1 and ls[i - 1] == '^':
            new_ls[len(new_ls) - 1] += ls[i]
        elif ls[i].isnumeric() or ls[i] == '.':
            if i > 0 and ls[i - 1].isnumeric() or ls[i - 1] == '.':
                new_ls[len(new_ls) - 1] += ls[i]
            elif i == 0 or ls[i - 1].isnumeric() or ls[i - 1] in '+-*':
                new_ls.append(ls[i])
            else:
                exit("Incorrect form of the equation")
        elif ls[i] in '+-*':
            if i == 0 and ls[i] == '*':
                exit("Symbol '*' can't be here")
            elif i > 0 and ls[i - 1] in '+-*':
                exit("Too many symbols '+', '-', '*' in a row")
            elif i == len(ls) - 1:
                exit("Incorrect form of the equation")
            new_ls.append(ls[i])
        elif ls[i].isalpha():
            ls_i_up = ls[i].upper()
            if tmp_ls and ls_i_up not in tmp_ls:
                exit("Too many variables")
            tmp_ls.append(ls_i_up)
            new_ls.append(ls_i_up)
        elif ls[i] == '^' and i > 0 and ls[i + 1] and ls[i + 1].isnumeric() and ls[i - 1].isalpha():
            new_ls[len(new_ls) - 1] += ls[i]
        else:
            exit("Incorrect form of the equation")
    for elem in tmp_ls:
        if elem != tmp_ls[0] and len(tmp_ls[0]) == 1:
            exit("Incorrect form of the equation")
    for i in range(len(new_ls)):
        if new_ls[i].count('.') > 1 or new_ls[i].find('^') != -1 and new_ls[i].count('.') > 0:
            exit("Incorrect data of the equation")
    checking_for_multiplictaion_signs(new_ls)
    return new_ls


def data_connection(side):
    new_ls, i = [], 0
    while i < len(side):
        if side[i] in '+-' and side[i + 1] and side[i + 1][0].isnumeric():
            if not '.' in side[i + 1]:
                new_ls.append(int(side[i] + side[i + 1]))
                i += 1
            else:
                new_ls.append(float(side[i] + side[i + 1]))
                i += 1
        elif side[i] in '-+' and side[i + 1] and side[i + 1][0].isalpha():
            new_ls.append(int(side[i] + '1'))
        elif side[i][0].isalpha() and i == 0:
            new_ls.append(1)
            new_ls.append(side[i])
        elif side[i][0].isalpha():
            new_ls.append(side[i])
        elif side[i] == '*' and side[i + 1].isnumeric():
            if isinstance(new_ls[len(new_ls) - 1], str) and new_ls[len(new_ls) - 1][0].isalpha():
                new_ls[len(new_ls) - 2] *= int(side[i + 1])
                i += 1
            else:
                new_ls[len(new_ls) - 1] *= int(side[i + 1])
                i += 1
        elif side[i].isnumeric():
            if new_ls and new_ls[len(new_ls) - 1].isnumeric():
                new_ls[len(new_ls) - 1] *= int(side[i + 1])
            new_ls.append(int(side[i]))
        i += 1
    return new_ls


def mod_number(num):
    return num if num >= 0 else -num


def square_root(num):
    n, i = float(0), 1
    while i > 0.0000001:
        while n * n <= num:
            n += i
        if n * n == num:
            return n
        n -= i
        i /= 10
    return n


def print_reduced_form(tokens):
    print('Reduced form:', end='')
    flag = 0
    if len(tokens) == 1 and tokens[0] == 0:
        return print(" 0 = 0")
    if tokens[0] == 0:
        flag = 1
    for key, value in tokens.items():
        if value == 0:
            continue
        if key == 0 and value > 0:
            print(' ', mod_number(value), sep='', end='')
        elif key == 0 and value < 0:
            print(' - ', mod_number(value), sep='', end='')
        elif key == 1 and value > 0 and flag == 1:
            flag = 0
            print(' ', mod_number(value), ' * X', sep='', end='')
        elif key == 1 and value > 0:
            print(' + ', mod_number(value), ' * X', sep='', end='')
        elif key == 1 and value < 0:
            print(' - ', mod_number(value), ' * X', sep='', end='')
        elif value > 0 and flag == 1:
            flag = 0
            print(' ', mod_number(value), ' * X^', key, sep='', end='')
        elif value > 0:
            print(' + ', mod_number(value), ' * X^', key, sep='', end='')
        elif value < 0:
            print(' - ', mod_number(value), ' * X^', key, sep='', end='')
    print(' = 0')
