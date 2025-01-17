x = [1,2,3]
for item in x:
    print(x[item-1])
#----------------------------
x2 = "HALLOU"
for i in x2:
    print(f'karakter {i}')
#----------------------------
x3 = [1,-2,-3,4,5,-2]
for i in x3:
    if i>0:
        print(f'{i} adalah positif')
    else:
        print(f'{i} adalah negatif')
#----------------------------
j = 0
for i in x3:
    j += i
    print(j)
print(j)
#----------------------------
y = [(1,2),(3,4)]
for a,b in y:
    print(a)
    print(b)
#----------------------------
y2 = {1:"a",2:"b"}
for (a,b) in y2.items():
    print(f'key {a}')
    print(f'value {b}')
#----------------------------
for i,it in enumerate(x):
    print(f'item ke-{i+1} adl {it}')
#----------------------------
for a,b in zip (x,x2):
    print(f'{a} dan {b}')
#----------------------------
for i in range(1,12):
    print(i)