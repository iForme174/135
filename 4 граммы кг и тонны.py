Stop = True
while(Stop):
    G = input("Введите граммы = ")
    if(G=="Q"):
        Stop = False
        continue
    KG = float(G)/1000.0
    T = float(G)/1000000.0



    print("Граммы =", G)
    print("Килограммы =", KG)
    print("Тонна =", T)

