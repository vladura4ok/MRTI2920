def brackets(text):
    if text[0] == ")":
        return False
    count = 0
    for j in text:
        if j == "(":
            count += 1
        elif j == ")":
            count += -1
            if count < 0:
                return False
    if count == 0:
        return True

    else:
        return False


def consider(x, y, sumb):
    if sumb == "+":
        return float(x) + float(y)
    elif sumb == "-":
        return float(x) - float(y)
    elif sumb == "*":
        return float(x) * float(y)
    elif sumb == "/":
        return float(x) / float(y)
