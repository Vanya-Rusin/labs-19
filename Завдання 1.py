s=[]
res=[]
r = 1
with open("text.TXT") as f:
    for row in f:
        numbers=list(map(float, row.split(' ')))
        res+=numbers
print(res)
s =0
for i in res:
    s+= i
m = s / len(res)
print(m)

