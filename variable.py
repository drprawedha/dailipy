# x, y, z = "orange", "banana", "cherry"
# print(x)
# print(y)
# print(z)
# print (x+y+z)

# Soal
# Buatkan soal untuk memperkenalkan diri anda

nama = 'Rhesa Prawedha'
umur = 33
tinggi = 1.73
aktif = True

print(nama)
print(umur,' tahun')
print(type(umur))


# ======================
# Contoh lain
kota = 'Surakarta'

# gabungkan string
sapaan = 'Halo, ' + nama + '!'
print(sapaan)

# menggunakan fstring yang lebih modern dan clean
sapaan2 = f'Halo, {nama}! Kamu dari {kota}!'
print(sapaan2)

# # Soal
# Simpan data berikut dalam variabel yang tepat:
# - nama (string)
# - umur (int)  
# - tinggi dalam meter (float)
# - apakah kamu pelajar? (bool)
# - 3 makanan favoritmu (list)

# Lalu cetak semua info ini dalam satu kalimat menggunakan f-string.
# Contoh output:
# "Nama: Andi, umur 20 tahun, tinggi 1.72m. Pelajar: True. Makanan favorit: ['nasi goreng', 'soto', 'bakso']"


fname = input('Nama Anda :')
print(type(fname))
fages = input('Umur Anda :')
# print(type(fages)) Control Perubahan
fagei = int(fages)
print(type(fagei))
ftalls = input('Tinggi :')
ftallf = float(ftalls)
print(ftallf)
print(type(ftallf))
fstatus = input('Apakah pelajar? (true/false)')
fstatusb = fstatus.lower() == 'ya'   # True kalau user ketik "ya", selain itu False
print(fstatusb)  # True atau False yang akurat
print(type(fstatusb))
makananfav = ['mie','bakso','burger']

result = f'Nama {fname}, umur {fagei}, tinggi {ftallf}m, Pelajar :{fstatusb}, Makanan Favorit {makananfav}'
print(result)
