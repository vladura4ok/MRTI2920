# _______1.Определил  количество пробелов между словами 2._Определили оптимальную длину пробелов____

def count_tab(text, num_str_):
    tab = 0
    b = 0
    tab_max = 0
    for i in text:
        len_i_str = len(i)
        b = b + len_i_str
        if b < num_str_:
            tab = tab + 1
        elif b >= num_str_:
            tab = tab - 1
            if tab > tab_max:
                tab_max = tab

            b = len(i)
            tab = 1
    return tab_max


def split_tab(a, tab):
    w, r = divmod(a, tab)
    return [w + (1 if j < r else 0) for j in range(tab)]


# ________________Считал текст, засплитил________________________
num_str_ = int(input("Enter the number of characters "))

while num_str_<15:
    num_str_ = int(input("Sorry, enter more than 15 characters "))
text_of_file = ""

with open("text.txt", "r", encoding="utf8") as file:
    for str_ in file:
        text_of_file = text_of_file + str_
text = text_of_file.strip().split()

tab_max = count_tab(text, num_str_)
# print("tab_max", tab_max)

# ------------------------Разобрался с количеством символов согласно  input-----------------------------------
num_str = num_str_
tab = 0
count_symb = 0
list_txt = []

for i in text:
    len_i_str = len(i)
    count_symb = count_symb + len_i_str
    if count_symb < num_str:
        list_txt.append(i)
        tab = tab + 1

    elif count_symb >= num_str:
        a_ = count_symb - len_i_str
        a = num_str + tab_max - a_
        tab = tab - 1

        # print("a", a)
        # print("tab", tab)
# -----------------------------------------------------------------------Пробелы--------------------------------------
        space_ = " "
        if tab == 0:
            tab = 1
        if a % tab == 0:
            c = int(a // tab)
            space = space_ * c
            line_width = space.join(list_txt)
            # print(line_width)

            with open("otvet_text_txt.txt", "a", encoding="utf8") as our:
                our.write(line_width + "\n")

        else:
            num_tab = split_tab(a, tab)
            count1 = 1
            u = 1
            for j in range(len(num_tab)):
                z = num_tab[j] * space_
                list_txt.insert(j + u, z)
                u = u + 1
            # print("".join(list_txt))

            with open("otvet_text_txt.txt", "a", encoding="utf8") as our:
                our.write("".join(list_txt) + "\n")


        list_txt.clear()
        list_txt.append(i)
        count_symb = len(i)
        tab = 1

# Концовка_________________________________________________________________

# print(" ".join(list_txt))
with open("otvet_text_txt.txt", "a", encoding="utf8") as our:
    our.write(" ".join(list_txt) + "\n")

print("Attention! Text written to file__otvet_text_txt.txt__")
