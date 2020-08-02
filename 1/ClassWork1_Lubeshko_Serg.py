# str = "two eleven seventeen two one thirteen ten four eight five nineteen"
# list_str = str.strip().split()
list_str = [x for x in input("enter a number in letters from 0 to 21 ").strip().split()]
list_num = []
count = -1
count_2 = -2
new_list = []
sum_odd = 0
# -----------------------------------------------------------------------------
for i in list_str:
    if i == "zero":
        list_num.append(0)
    elif i == "one":
        list_num.append(1)
    elif i == "two":
        list_num.append(2)
    elif i == "three":
        list_num.append(3)
    elif i == "four":
        list_num.append(4)
    elif i == "five":
        list_num.append(5)
    elif i == "six":
        list_num.append(6)
    elif i == "seven":
        list_num.append(7)
    elif i == "eight":
        list_num.append(8)
    elif i == "nine":
        list_num.append(9)
    elif i == "ten":
        list_num.append(10)
    elif i == "eleven":
        list_num.append(11)
    elif i == "twelve":
        list_num.append(12)
    elif i == "thirteen":
        list_num.append(13)
    elif i == "fourteen":
        list_num.append(14)
    elif i == "fifteen":
        list_num.append(15)
    elif i == "sixteen":
        list_num.append(16)
    elif i == "seventeen":
        list_num.append(17)
    elif i == "eighteen":
        list_num.append(18)
    elif i == "nineteen":
        list_num.append(19)
    elif i == "twenty":
        list_num.append(20)
    elif i == "twenty-one":
        list_num.append(21)
list_sort = sorted(list(set(list_num)))
# list_sort = list(list_sort)
# list_sort.sort()
print("#1,2. Eliminated duplicates and ascending sorting: ", *list_sort)
# -----------------------------------------------------------------------------
list_sort.sort(reverse=True)
if len(list_sort) == 1:
    print("#3.Multiplication of the first and second the sum of the second and third, etc. :", list_sort[0])
    new_list.append(list_sort[0])
else:
    while count_2 >= -len(list_sort):
        num = list_sort[count] * list_sort[count_2]
        new_list.append(num)
        count -= 1
        count_2 -= 1
        if count == -len(list_sort):
            break
        num = list_sort[count] + list_sort[count_2]
        new_list.append(num)
        count -= 1
        count_2 -= 1
    print("#3. Mult. of the first and second the sum of the second and third, etc. (new list): ", *new_list)
# -----------------------------------------------------------------------------
for j in new_list:
    if j % 2 != 0:
        sum_odd = sum_odd + j
print("#4. Sum of odd numbers (in new_list): ", sum_odd)
