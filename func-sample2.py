
# return value 

def hitung_belanja(harga, jumlah, diskon=0):
    subtotal = harga * jumlah
    potongan = subtotal * diskon
    total = subtotal - potongan
    return total

def info_belanja(harga, jumlah, diskon=0):
    total = hitung_belanja(harga,jumlah, diskon)
    return {
        "subtotal" : harga * jumlah,
        "potongan" : harga * jumlah * diskon,
        "total"    : total
    }

tagihan = info_belanja(20000,3, diskon=0.1 )
print(tagihan["total"])
print(tagihan)
