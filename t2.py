text = 'five thiteen two eleven seventeen two one thirteen ten four eigtht five nineteen'
a = text.split()
d = {
    a[0] : 5,
    a[1] : 13,
    a[2] : 2,
    a[3] : 11,
    a[4] : 17,
    a[5] : 2,
    a[6] : 1,
    a[7] : 13,
    a[8] : 10,
    a[9] : 4,
    a[10] : 8,
    a[11] : 5,
    a[12] : 19
} # 0. task
#for k, v in d.items():
   # print(v) where is five?
ab = sorted(set(d.values())) # 1. , 2. task

print("-----Task 3 -----") # 3. task

for i in range(len(ab)):
    if i < len(ab) -1:    
        if i % 2 != 0:
            print('{0}   +'.format(ab[i]+ab[i+1]))   
        else:
            print('{0}   *'.format(ab[i]*ab[i+1]))
   
    print("---------")
print(ab)
# 4 task
sum = 0
for e in ab:
    if e % 2 != 0:
        sum += e
print('\n4.task =   {0} '.format (sum))
