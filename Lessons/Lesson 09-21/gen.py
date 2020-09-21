def gen():

    print("first")
    yield 1

    print("second")
    yield 2

    return "smtng"

    print("third")
    yield 3

def strgen(my_string):
    for i in range(len(my_string)-1, -1, -1):
        yield my_string[i]

def fibbonaci(limit):
    x, y = 0, 1
    for i in range(limit):
        x, y = y, x+y
        yield x
        
#g = gen()
#iter(g)
#print(g)
#for i in g:
#    print(i)

#strg = strgen("my test string")
#for i in strg:
#    print(i)

fib = fibbonaci(10)
for i in fib:
    print(i)