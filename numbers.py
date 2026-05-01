# sample number pada umumnya
print(2)
print(200)
print(3230)

# sample aritmatik
print('penjumlahan = 1 + 2')
print(1+2)
print('pengurangan = 2 - 2')
print(2-2)
print('pembagian 5/3 dan float')
print(float(5/3))
print('pembagian 5/3 dan int')
print(int(5/3))

# sample mix text dan number
print('sample mix teks dan nomor')
print('i am',33,'years old.')

print('pembulatan 10//3')
print(10//3)

print('modulis di 11 % 5')
print(11%5)

# print(2**2)
print('contoh 2pangkat3 ')
print(2**3)

x = 0.1 + 0.2
print('contoh 0.1+0.2=0.3')
print(x)
print(x==0.3)
#error karena tidak ada representasi binnernya

x1 = 1 + 2
print('contoh 1+2=3')
print(x1)
print(x1==3)
#tidak error karena merepresentasi binner


# lain lain
# abs = absolut jika float biasa
# round untuk kisaran berapa digit dibelakang koma
print(abs(-15), round(3.567, 2))

z = 7 + 24j
print(z.real, z.imag, abs(z))

# contoh diatas mengacu pada pythagoras
# abs() selalu mengukur seberapa jauh suatu nilai dari nol — baik di garis bilangan (int/float) maupun di bidang koordinat (complex).

print("3 + 4 * 2 ** 2 - 1")
print("3 + (4 * (2 ** 2)) - 1")
print(3 + 4 * 2 ** 2 - 1)
print(3 + (4 * (2 ** 2)) - 1)

import math
print(math.ceil(4.1), math.floor(4.9), math.trunc(-3.7))

# math.ceil(4.1) → 5
# 4.1 → 5
#         ↑ naik ke atas
# ──────┬──────┬──────
#       4    [4.1]   5


# math.floor(4.9) → 4
# 4.9 → 4
#   ↓ turun ke bawah
# ──────┬──────┬──────
#       4   [4.9]   5

# math.trunc(-3.7) → -3
# -3.7 → -3
#          ↑ menuju nol
# ──────┬──────┬──────
#      -4  [-3.7]  -3    0