import re
import sys
import my_module


# _________________________________________
def level(lev):  # Определим уровень операции
    if lev == "+" or lev == "-":
        return 1
    elif lev == "*" or lev == "/":
        return 2
    elif lev == "(":
        return 0


# -----------------------Польская нотация------------------------------------

def rev_pol(s):
    token = re.findall(r'([\d.]+|\W)', s)
    stack_o = []
    stack_num = []
    operat = ["+", "-", "*", "/", "(", ")"]

    for i in token:
        if i == "(":
            stack_o = [i] + stack_o
        elif i in operat:
            if not stack_o:
                stack_o = stack_o + [i]
            elif i == ")":
                while True:
                    q = stack_o[0]
                    stack_o = stack_o[1:]
                    if q == "(":
                        break
                    stack_num += [q]
            elif level(stack_o[0]) < level(i):  # Обратился к функции уровня
                stack_o = [i] + stack_o
            else:
                while True:
                    if not stack_o:
                        break
                    q = stack_o[0]
                    stack_num += [q]
                    stack_o = stack_o[1:]
                    if level(q) == level(i):
                        break
                stack_o = [i] + stack_o
        else:
            stack_num.append(float(i))
    while stack_o:
        q = stack_o[0]
        stack_num += [q]
        stack_o = stack_o[1:]
    return stack_num


# -------------------------------------------------------------------
flag = True
while flag:
    calc = input("ENTER a numeric expression. FLOAT numbers with a dot ")  # (-4+3)*(-12+(2-1))
    calc = calc.replace("(-", "(0-")
    if calc[0] == "-":
        calc = "0" + calc

    # ________________________Проверка на скобки_____________________________
    if my_module.brackets(calc):  # if brackets(calc) == True:
        str_list = rev_pol(calc)
    else:
        print()
        sys.exit("Brackets are incorrect")

    # print(*rev_pol(calc))

    # -------------------------------Распаковка польской нотации----------
    str_list = rev_pol(calc)

    len_ = len(str_list)
    min_a = len_
    operator = ["-", "+", "*", "/"]
    while len_ > 1:
        for _ in operator:
            if _ in str_list:
                a = str_list.index(_)  # номер индекса
                if a < min_a:
                    min_a = a
        sumb = str_list[min_a]
        x = str_list[min_a - 2]
        y = str_list[min_a - 1]
        try:
            G = my_module.consider(x, y, sumb)
        except:
            print("Expression entered incorrectly")  # Выражение введено не верно
            str_list = str_list.clear()
            break
        del str_list[min_a]
        del str_list[min_a - 1]
        del str_list[min_a - 2]
        str_list.insert(min_a - 2, G)
        len_ = len(str_list)
        min_a = len_
    try:
        print(*str_list)
    except:
        pass
    if input("!!!!Press number 0 to continue!!!") == "0":
        flag = True
    else:
        flag = False
    # print(len_)
    # print("min_a", min_a)
