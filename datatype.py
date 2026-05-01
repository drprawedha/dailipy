# mendapat type data
x = "nama"
y = 5
z = 0.3

print(type(x))
print(type(y))
print(type(z))

# output
# <class 'str'>
# <class 'int'>
# <class 'float'>

# catatan
# str > untuk tulisan, kata, kalimat

# int > untuk bilangan bulat, tanpa desimal, index, dll

# float > angka dengan koma -- harga, berat, nilai, dll

# complex > khusus untuk komputasi ilmiah

# list > kumpulan data  yang bisa diubah
# contoh :
belanjaan = ['apel', 'bayam', 'cabe']
belanjaan.append('daging') #bisa ditambah
# lihat hasilnya disini :
print(belanjaan)

# tuple > kumpulan data yang tetap, seperti list tapi tidak bisa dirubah, contoh koordinat, urutan hari
hari = ('senin', 'selasa', 'rabu')

# range > urutan angka, untuk perulangan / membuat deret angka
for i in range(1, 9):  # 1 2 3 4 5 ... 8 berhenti di 9 
    print(i)

# dict > atau dictionary, untuk menyimpan data yang punya label / nama. contohnya formulir
siswa = {
    'nama' : 'adni',
    'umur' : 30,
    'jurusan' : 'Informatika'
}
print(siswa['nama'])
print(siswa['jurusan'])

# set < kumpulan unik tanpa urutan, untuk menyimpan data tanpa duplikat. atau operasi himpunan, irisan, gabungan
hobi = {'baca', 'coding', 'mancing', 'mancing'}
print(set(hobi)) #{'baca', 'coding', 'mancing'}

# frozenset > set yang tidak bisa diubah
category = frozenset({'buah','sayur'})
buah = frozenset({"apel", "mangga", "jeruk"})
print(buah)
# → frozenset({'apel', 'mangga', 'jeruk'})
# sample
# buah.add("pisang")     # → AttributeError
# buah.remove("apel")    # → AttributeError
# buah.clear()           # → AttributeError

# bool -- nilai benar / salah
# untuk kondisi, percabangan, dan logika
sudah_login = True
if sudah_login:
    print("Selamat datang!")

# bytes / bytearray / memoryview — data biner
# 1. Enkripsi & keamanan data
# 2. Kirim & terima data lewat jaringan (socket)
# 3. Baca file gambar / PDF / video
# 4. Kompresi file
# 5. Komunikasi dengan perangkat keras (Arduino, sensor)
# 6. Encode gambar ke Base64 (untuk API / web)
# ......

# None
hasil = None  # belum ada hasil
if hasil is None:
    print("Belum diproses")