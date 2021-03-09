####### hesap makinesi modülü ###############

def toplama(a,b):
    return a+b

def çıkarma (a,b):
    return a-b

def çarpma (a,b):
    return a*b

def bölme (a,b):
    return a/b

def aşağıyuvarla(a):
    return a//1

def yukarıyuvarla(a):
    return (a//1)+1

def karekök(a):
    return a**0.5

def mod(a,b):
    return a%b

def faktöriyel(a):
    faktoriyel=1
    a=int(a)
    for i in range(1, a + 1):
        faktoriyel *= i
    return faktoriyel

def ebob(a,b):
    if a==1:
        return b
    elif b==1:
        return a
    else:
        sayı1_bolenler=list()
        sayı1_bolenler=bolenler(a)
        sayı2_bolenler=list()
        sayı2_bolenler=bolenler(b)
        ortak_bolen=list()
        for i in sayı1_bolenler:
            for x in sayı2_bolenler:
                if i==x:
                    ortak_bolen.append(x)
        sorted(ortak_bolen)
        return ortak_bolen[-1]

def hipotenüs(a,b):
    return (a**2+b**2)**0.5

def bolenler(sayı):
    a = list()
    for i in range(1,sayı + 1):
        if sayı % i == 0:
            a.append(i)
    return a
