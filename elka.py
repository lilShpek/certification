n = int(input("Введиите n : "))

for i in range(1,n+1):
    print(' ' *(n-i) + (i*2-1) * '*')

i = 2
for i in (2,6):
    for j in range(2,11):
        s = ''
        for k in range(i, i+4):
            s += f'{k} x {j:<2} = {k*j:<2} \t\t'
        print(s)
    print()