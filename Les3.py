from operator import truediv

x=5
while x>0:
    print(f'iterasi ke- {x}')
    x-=1
else:
    print("done")
# -----------------------
x2 = [1, 2, 3, 4, 5]
for i in x2:
    if i == 2:
        pass
    else:
        print(i)
print("-------------------------")
#-----------------------
x2 = [1,2,3,4,5]
for i in x2:
    if i == 2:
        continue
    else:
        print("x2 =")
        print(i)
print("-------------------------")
#-----------------------
x3 = 5
while True:
    print("yo")
    x3-=1
    if x3==0:
        break
print("-------------------------")
