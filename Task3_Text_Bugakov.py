mytext = open(r"C:\\Users\\User\\Desktop\\111\\text.txt", mode ='r+', encoding='utf-8')
oldtext = mytext.read()
newtext = (oldtext.replace('\n', ' '))
newtext.close()
new = open(r"C:\\Users\\User\\Desktop\\111\\text2.txt", mode ='w', encoding='utf-8')
new.write(newtext)
new.close()
new = open(r"C:\\Users\\User\\Desktop\\111\\text2.txt", mode ='r+', encoding='utf-8')
limit = int(input())
if limit <= 15:
    print('error')
else:
    f = new.read()
    for x in range (0, len(f), int(limit)):
        s = f[x:x+limit]


        
        n = s.split(" ")
        print(" ".join(n))