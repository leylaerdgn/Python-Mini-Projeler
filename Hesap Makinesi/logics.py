def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def bol(a,b):
    if b==0:
        return "Sıfıra Bölme Hatası"
    return a/b

print(topla(5, 3))
print(bol(10, 2))
print(bol(10, 0))