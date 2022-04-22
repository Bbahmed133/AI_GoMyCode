from dataclasses import replace
import math

C, H = 50, 30
def funct(c,d,h):
    l = []
    d = d.split(',')
    for i in d:
        x = int(i)
        l.append(math.sqrt((2*c*x)/h))
    ch = ""
    for i in l:
        ch += str(math.trunc(i)) + ','
    return ch[0:len(ch)-2]    

D = input('type different values seperated by , (ex : 180,150,120)')


print(funct(C,D,H))    