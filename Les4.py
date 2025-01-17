v = "selamat"
list_var = [i for i in v]
print(list_var)

list_var2 = [i for i in range(1,5)]
print(list_var2)

list_var3 = [i for i in range(20,0,-3)]
print(list_var3)

x = [1,2,3]
y = [10,20,30]
xy= [a*b for a in x for b in y]
print(xy)


list_var4 = [i for i in x if i%2==1]
print(list_var4)

list_var5 = ["ganjil" if i%2==1 else i for i in x]
print(list_var5)