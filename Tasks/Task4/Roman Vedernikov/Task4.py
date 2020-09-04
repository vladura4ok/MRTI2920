def summ (arr, s=0):

    for i in range (len(arr)):

        if type(arr[i]) == list:
            s = s + summ(arr[i])

        else:
            s = s + arr[i]

    return s

arr= [1, 2, [5, 6, [8, 9]], 18]

b = summ(arr)

print("The sum of all items in the list", b)