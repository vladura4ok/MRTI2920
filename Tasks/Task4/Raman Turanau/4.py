
b = []
a = 0
arr=[1, 2, [2, 4, [[7, 8], 4, 6]]]

def unpacking(arr):
    for i in range (len(arr)):
        if type(arr[i]) is int:
            b.append(arr[i])
        else:
            c = arr[i]
            unpacking(c)
    return(b)

unpacking(arr)
for i in range(len(b)):
    a += b[i]
print(a)

            


input("print enter to exit")