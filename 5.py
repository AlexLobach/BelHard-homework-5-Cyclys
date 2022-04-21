class NonNumericError (ValueError):
    pass

class InconsistentDataError (Exception):
    pass

a = []
b = []
try:
    for f1 in input('Введите первые катеты a: ').split():
        a.append(float(f1))

    for f2 in input('Введите первые катеты b: ').split():
        b.append(float(f2))
except:
    raise NonNumericError ("Введены не числа")

if len(a)!= len(b):
    raise InconsistentDataError ("Массивы с катетами имеет разную длинну")


hipp = [((c1**2 + c2**2)**0.5) for c1,c2 in zip(a, b)]
area = [((s1*s2)/2) for s1,s2 in zip (a, b)]


for num ,k, v, cat1, cat2 in zip(range(1, len(a)+1), hipp, area, a, b):
    print ( "Треугольник",num, "с катетами",cat1,
    "и" ,cat2, "имеет площадь",v,"и гиппотинузу",k,"")

