# Известен ГОД. Определить, будет ли этот год високосным, и к какому веку этот год относится
y = int(input("Введите год для проверки "))
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Год високосный ")
else:
    print("Год невисокосный")
if y % 100 == 0:
    y = y // 100
    print(y," век")
elif y % 100 != 0:
    y = (y // 100) + 1
    print(y," век")
