import random as rn
z=int(input("Ввести кількість елементів масиву:"))
b=int(input("Введіть початок діапазон: "))
c = int(input("Введіть кінець діапазон: "))
a=[]
for i in range(z):
    a.append(rn.randint(b,c))
print("Масив:", a)
k = int(input("Введіть число для порівняння:"))
s = 0
for i in range(z):
    if a[i] < k:
        s = s + a[i]
print("Сума елементів:", s)
