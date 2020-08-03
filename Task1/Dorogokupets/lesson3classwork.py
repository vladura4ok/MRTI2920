#1 - from words to numbers
control = [['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7], ['eight', 8], ['nine', 9], ['ten', 10], ['eleven', 11], ['twelve', 12], ['thirteen', 13], ['fourteen', 14], ['fifteen', 15], ['sixteen', 16], ['seventeen', 17], ['eighteen', 18], ['nineteen', 19], ['twenty', 20], ['twenty-one', 21]]

method = input('do you want to enter numbers? type letter "y" for "yes" or "n" for "no": ')
if method == 'y':
	numbers = input('please input several numbers as you wish from 1 to 21 included, in letters separated by a spacebar: ')
elif method == 'n':
	numbers = 'eleven one four one eight sixteen twenty-one'
else:
	print('you entered wrong letter')

numlist = numbers.split()
x = len(numlist)
y = len(control)

intnum = []
for i in range(0, x):
	for j in range(0, y):
		if control[j][0] == numlist[i]:
			intnum.append(control[j][1])

#2 - sort numbers
newlist = list(set(intnum))
intnum = sorted(newlist)

#3 - hard calculations
z = len(intnum)
result1 = 0

for i in range(0, z):
	if i == (z - 1):
		break
	elif i == 0:
		result1 = result1 + intnum[i] + intnum[i + 1]
	elif (i % 2) != 0:
		result1 = result1 + intnum[i] * intnum[i + 1]
	elif (i % 2) == 0 and i != 0:
		result1 = result1 + intnum[i] + intnum[i + 1]
print(result1)

#4 - sum of odd numbers
result2 = 0
for i in intnum:
	if i % 2 == 0:
		result2 = result2 + i
print(result2)