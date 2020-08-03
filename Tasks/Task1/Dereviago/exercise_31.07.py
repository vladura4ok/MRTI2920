"""
* at run, comment on either 3 or 4 tasks; cannot run together because the array is deleted as it passes (in the 3rd or 4th task).
"""


result = input().split(" ")
while isinstance(result[0], str):
    result.append({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
         'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
         'eighteen': 18, 'nineteen': 19, 'twenty': 20}[result[0]])
    del result[0]
print(result)


""" 1-2. вывести уникальные значения + отсортировать """
result = sorted(list(set(result)))
print(result)


""" 3. вывод суммы / произведения"""
try:
    while len(result):
        print(result[0] + result[1])
        del result[0]
        print(result[0] * result[1])
        del result[0]
except IndexError:
    print('Array is empty')


# """ 4. вывести полную сумму всех нечетных чисел """
# result.append(False)
# result.append(0)
# while result[0]:
#     if result[0] % 2 != 0:
#         result[-1] += result[0]
#     del result[0]
# else:
#     del result[0]
# print(result)
