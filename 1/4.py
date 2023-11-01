s = input("Введите последовательность чисел через пробел: ")
ns = s.split()

s_n = set()

for n in ns:
    if n in s_n:
        print("YES")
    else:
        print("NO")
        s_n.add(n)
