arrey=[]
g = []
with open('text2.TXT') as ff:
    for row in ff:
        numbers = list(map(float, row.split(',')))
        arrey += numbers
    for el in arrey:
        if el<0:
            g.append(el)
print(arrey)
print(g)
print("Найбільший елемент серед від’ємних=",max(g))
with open('v.dat', 'w') as ff:
    ff.write(str(g))