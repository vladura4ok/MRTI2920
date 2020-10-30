def max_of_brakets(string):
    max_of_brakets = 0
    list_of_brakets = []
    for i in string:
        if i == "(":
            max_of_brakets += 1
        elif i == ")":
            list_of_brakets.append(max_of_brakets)
            max_of_brakets = 0
    return max(list_of_brakets)


def raskukoz_op(v, op):
    v = v.replace('+-', '-')
    v = v.replace('--', '+')
    v1_splitted = v.split(op)
    v1 = []
    for i in v1_splitted:
        v1.extend([i, op])
    v1 = v1[:-1]
    return v1


def raskukoz(v):
    res = raskukoz_op(v, '*')
    result = []
    for item in res:
        res1 = raskukoz_op(item, '/')
        for item1 in res1:
            res2 = raskukoz_op(item1, '+')
            for item2 in res2:
                res3 = raskukoz_op(item2, '-')
                result.extend(res3)
    return result


def calculate(v_rask):
    result = v_rask[:]
    while "*" in result:
        index_of_first_op = result.index("*")
        a = float(result[index_of_first_op -1]) * float(result[index_of_first_op + 1])
        result[index_of_first_op -1 : index_of_first_op + 2] = [a]
    while "/" in result:
        index_of_first_op = result.index("/")
        a = float(result[index_of_first_op -1]) / float(result[index_of_first_op + 1])
        result[index_of_first_op -1 : index_of_first_op + 2] = [a]
    while "-" in result:
        index_of_first_op = result.index("-")
        a = float(result[index_of_first_op -1]) - float(result[index_of_first_op + 1])
        result[index_of_first_op -1 : index_of_first_op + 2] = [a]
    while "+" in result:
        index_of_first_op = result.index("+")
        a = float(result[index_of_first_op -1]) + float(result[index_of_first_op + 1])
        result[index_of_first_op -1 : index_of_first_op + 2] = [a]
    return result[0]


def simplify(v):
    brakets = max_of_brakets(v)
    max_of_brakets2 = 0
    for indx, i in enumerate(v):
        if i == "(":
            max_of_brakets2 += 1
        elif i == ')':
            max_of_brakets2 -= 1
        if max_of_brakets2 == brakets:
            break
    for indx2, i2 in enumerate(v[indx:]):
        if i2 == ")":
            break
    indx2 += indx

    v_rask = raskukoz(v[indx+1:indx2])
    calced = calculate(v_rask)
    v = v[:indx] + str(calced) + v[indx2+1:]
    return v


v = input('Enter the calcultion: ')

while '(' in v:
    v = simplify(v)

result = calculate(raskukoz(v))
print(result)
