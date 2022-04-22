ch = input('type something: ')
n = -1

while not(n in range(0,len(ch)-1)):
    x = input('type the index of the character that you wanna delete: ')
    for i in range(0,len(x)-1):
        if (x[i] >= '0')and(x[i] <= '9'):
            n = int(x)
        else:
            n = -1



print(ch.replace(ch[n],''))