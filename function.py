# pertama, belajar anatominya dulu
def sapa(nama):                                  # def = define, 'nama' = parameter
    pesan = f'\nHalo, {nama}! \nSalam Kenal'
    return pesan                                 # return = kirim balik nilai

nama = input('Siapa nama anda ? ')
hasil = sapa(nama)                              # panggil fungsi, simpan hasilnya
print(hasil)                                    # Hasilnya