def Sum(arr):
    try:
        x = 0
        for i in arr:
            x += Sum(i)
        return x
    except TypeError: 
        return arr

print(Sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))
