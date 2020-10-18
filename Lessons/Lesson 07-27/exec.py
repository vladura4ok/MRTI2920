"author - Пилипенок Мифодий Владимирович"
q = input("Enter your example:")

if '+' in q:
    ls = q.split('+')
    print(int(ls[0])+int(ls[1]))
if '-' in q:
    ls = q.split('-')
    print(int(ls[0])-int(ls[1]))
if '/' in q:
    ls = q.split('/')
    print(int(ls[0])/int(ls[1]))
if '*' in q:
    ls = q.split('*')
    print(int(ls[0])*int(ls[1]))
else:
    print("added int")