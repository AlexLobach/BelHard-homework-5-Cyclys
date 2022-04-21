cath = []

for f1 in input('Введите катеты: ').split():
    cath.append(float(f1))
print (cath)


hipp = [((c1**2 + c2**2)**0.5) for c1,c2 in zip(cath[::2], cath[1::2])]
area = [((s1*s2)/2) for s1,s2 in zip (cath[::2], cath[1::2])]

for num ,k, v, cat1, cat2 in zip(range(1, len(hipp)+1),
 hipp, area, cath[::2], cath[1::2]):
    print ( "Треугольник",num, "с катетами",cat1,
    "и" ,cat2, "имеет площадь",v,"и гиппотинузу",k,"")