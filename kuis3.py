def func_luas_keliling_lingkaran(phi,r):
    luas = phi*r*r
    keliling = 2*phi*r
    return luas, keliling

luas_keliling = func_luas_keliling_lingkaran(22/7,7)
L = luas_keliling[0]
k = luas_keliling[1]
print(luas_keliling)
print(L)
print(k)