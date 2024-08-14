def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

a = 20
b = 86
print("El MCD de", a, "y", b, "es", mcd(a, b))
#Holaaaa
