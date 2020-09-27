z = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 
'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
a = "five thirteen two eleven seventeen two one thirteen ten four eight nineteen"
b = a.split(' ')
c = []
for num_str in b:
    num = z[num_str]
    c.append(num)
d = set(c)
e = sorted(d)
print(e)
print()
for i in range(len(e)):
    if i+1 != len(e):
        if i % 2 == 0:
            f = e[i] * e[i+1]
        else:
            f = e[i] + e[i+1]
        print(f)
print()
g = 0
for i in range(len(e)):
    if e[i] % 2 != 0:
        g += e[i]
print(g)









