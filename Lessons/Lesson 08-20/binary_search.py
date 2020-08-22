x = [1,2,3,4,5,6,7,8,9]

def search(arr, elem, start=0, end=None):
    if end == None:
        end = len(arr)-1
    if start > end:
        return -1

    mid = (start + end)//2

    if elem == arr[mid]:
        return mid

    if elem < arr[mid]:
        return search(arr, elem, start, mid - 1)

    return search(arr, elem, mid + 1, end)

print(search(x, 8))