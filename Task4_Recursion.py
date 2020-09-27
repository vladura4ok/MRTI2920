def sum(mylist):
    totalsum = 0
    for i in mylist:
        if type(i) == type([]):
            totalsum = totalsum + sum(i)
        else:
            totalsum = totalsum + i
    return totalsum
print("Sum is:", sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))
