#1-Calcule as seguintes expressões:
print(20 // 3 + 4)
print(not('x'=="x"))
print(4 >= 5 and 9 <=9)
print(4 % 3 == 1 or False) 
#2-Qual a saída do seguinte programa?
a = 5
b = 6
if a + b > 11:
    print("x") 
elif a + 2 == 8:
    print("y")
else: 
    print("z")
#3-Qual a saída?
x = 1
y = 1 
while x < 5:
    x = x + 2

for i in range(x) : 
    y =y + i
print(x + y)
#4-Qual a saída?
lista = [2, 4, 6, 8]
lista.append(7)
x = len(lista)
y = lista[x-1]
print(x+y)