z = int(input("Enter number of symbols:"))
def fib(n):
    if n in (1, 2):
        return 1
    return (fib(n - 1) + fib(n - 2))
m = [i for i in range(1,z+1)]
k = list(map(fib, m))
print('fib'+'('+str(z)+'):', k)