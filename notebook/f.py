def fibonacci(n):
    if n<2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n_jmlh = int(input("input n deret : "))
tmp = []
for i in range(n_jmlh):
   tmp.append(fibonacci(i))
print(tmp)