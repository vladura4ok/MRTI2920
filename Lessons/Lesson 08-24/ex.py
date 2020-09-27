def get_value_or_default(default):

    def getter(arr, index):

        assert index > 0, "x must be positive"

        if arr is None or len(arr) == 0:
            raise Exception("the collection is empty")

        try:
            return arr[index]
        except IndexError:
            return default
        finally:
            arr.clear()
    
    return getter

get_value1 = get_value_or_default("_")
get_value2 = get_value_or_default("")
get_value3 = get_value_or_default("0")

x = [1,2,3,4,5]

try:
    print(get_value1(x, -1))
except Exception as er:
    print(er)

print(x)





