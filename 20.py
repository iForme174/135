# Дано число X. Определить, принадлежит ли это число заданному промежутку [a,b].
x = int(input("Введите число для проверки "))
a = int(input("Укажите начало промежутка "))
b = int(input("Укажите начало промежутка "))
if a <= x <= b:
    print("Число ",x, " Принадлежит множеству [",a,",",b,"]")
else:
    print("Число ",x, " не принадлежит множеству [",a,",",b,"]")
