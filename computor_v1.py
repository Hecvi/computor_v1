import computor_v1_2 as comp


def tokenize(ls, tokens):
    for i in range(len(ls)):
        if not isinstance(ls[i], str) and (i + 1 == len(ls) or not isinstance(ls[i + 1], str)):
                tokens[0] += ls[i]
        elif not isinstance(ls[i], str) and ls[i + 1] and isinstance(ls[i + 1], str):
            find_degree = ls[i + 1].find('^')
            if find_degree == -1:
                tokens[1] += ls[i]
            else:
                tokens[int(ls[i + 1][2:])] += ls[i]


def finding_maximum_degree(ls):
    max_val, flag = -1, 0
    for elem in ls:
        if isinstance(elem, str):
            flag = 1
            position = elem.find('^')
            if position != -1:
                cross = int(elem[2:])
                if cross > max_val:
                    max_val = cross
            elif position == -1 and max_val < 1:
                max_val = 1
    if flag == 0:
        return 0
    return max_val


def degree_above_two(tokens):
    degree = 0
    for key, value in tokens.items():
        if value != 0:
            degree = key
    print("Polynomial degree:", degree)
    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve")
        exit(0)


def adding_coefficients(tokens):
    coeff = {'a': 0, 'b': 0, 'c': 0}
    for key, value in tokens.items():
        if key == 0:
            coeff['c'] = value
        elif key == 1:
            coeff['b'] = value
        elif key == 2:
            coeff['a'] = value
    return coeff


def solving_equation(coeff):
    if coeff['a'] == coeff['b'] == coeff['c'] == 0:
        print("The equation has an infinite number of solutions")
        exit(0)
    if coeff['a'] == coeff['b'] == 0:
        print("No solutions")
        exit(0)
    if coeff['a'] == 0:
        print("The solution is:")
        print(round(-coeff['c'] / coeff['b'], 6))
        exit(0)
    d = coeff['b'] * coeff['b'] - 4 * coeff['a'] * coeff['c']
    if d < 0:
        print("Discriminant is negative. Complex roots of the equation are:")
        num = round(comp.square_root(comp.mod_number(d)) / (2 * coeff['a']), 6)
        print(round(-coeff['b'] / (2 * coeff['a']), 6), '-', num, '* i')
        print(round(-coeff['b'] / (2 * coeff['a']), 6), '+', num, '* i')
    elif d == 0:
        print("Discriminant is zero. There is one solution:")
        print(round(-coeff['b'] / (2 * coeff['a']), 6))
    elif d > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(round((-coeff['b'] - comp.square_root(d)) / (2 * coeff['a']), 6))
        print(round((-coeff['b'] + comp.square_root(d)) / (2 * coeff['a']), 6))


if __name__ == "__main__":
    buf_str = input()
    if not buf_str or buf_str == '':
        exit("Where is anything? Try again")
    if buf_str.find('=') == -1:
        exit("Where is '=' symbol? Try again")
    if buf_str.count('=') > 1:
        exit("Too many symbols '='. Try again")
    for elem in ' \t\v\r\n\f\a\b':
        buf_str = buf_str.replace(elem, '')
    buf_str = buf_str.replace(',', '.')
    before_equal, after_equal = buf_str.split('=')
    ls_left = comp.data_connection(comp.checking_correctness(list(before_equal)))
    ls_right = comp.data_connection(comp.checking_correctness(list(after_equal)))
    for i in range(len(ls_right)):
        if isinstance(ls_right[i], int):
            ls_right[i] *= -1
    ls_left.extend(ls_right)
    tokens = dict.fromkeys(list(range(finding_maximum_degree(ls_left) + 1)), 0)
    tokenize(ls_left, tokens)
    comp.print_reduced_form(tokens)
    degree_above_two(tokens)
    solving_equation(adding_coefficients(tokens))
