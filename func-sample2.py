
# return value 

## Main Program

def calculate_total(price, qty, discount=0):
    subtotal = price * qty
    deduction = subtotal * discount
    total = subtotal - deduction
    return total     # call angka

def calculate_change(total,paid):
    if paid < total :
        return -1
    return paid - total

# def get_receipt(price, qty, discount=0):
#     total = calculate_total(price,qty, discount)
#     return {         # call dict
#         "subtotal" : price * qty,
#         "deduction" : price * qty * discount,
#         "total"    : total
#     }

# def print_line(char='-', lenght=30):
#     print(char * lenght)

# print_line()
# print_line('=',30)

# receipt = get_receipt(20000,3, discount=0.1 )
# print(receipt["total"]) # get value total only
# print(receipt)

# Fungsi 1 — hitung_total(harga, jumlah)
#   → kembalikan total harga

# Fungsi 2 — hitung_kembalian(total, bayar)  
#   → kembalikan kembalian
#   → kalau bayar kurang dari total, kembalikan -1

# Fungsi 3 — cetak_struk(nama_barang, harga, jumlah, bayar)
#   → panggil fungsi 1 dan 2 di dalamnya
#   → cetak struk seperti ini:

def print_receipt(items,paid):
    print("============================")
    print('       struk belanja')
    print("============================")

    grand_total = 0
    for item in items:
        total = calculate_total(item['price'],item['qty'])
        grand_total += total
        print(f"Barang  : {item['name']}")
        print(f"Harga   : Rp {item['price']}")
        print(f"Qty     : {item['qty']}")
        print(f"Total   :   Rp {total}")
        print("============================")

    change = calculate_change(grand_total, paid)
    print(f"Grand Total : {grand_total}")
    print(f"Paid        : {paid}")
    print(f"Change      : {change}")
    print("=============================")

def add_item():
    name = input("Nama barang : ")
    price = int(input("Harga "))
    qty   = int(input("Jumlah "))
    return {
        "name": name, 
        "price": price, 
        "qty":qty}

# --- main program ---
items = []

while True:
    print("\n1. Tambah transaksi")
    print("2. Cetak struk & selesai")
    choice = input("Pilihan: ")

    if choice == "1":
        items.append(add_item())
    elif choice == "2":
        paid = int(input("Jumlah bayar: "))
        print_receipt(items, paid)
        break
    else:
        print("Pilihan tidak valid.")

# ================================
#         STRUK BELANJA
# ================================
# Barang  : Indomie
# Harga   : Rp 3500
# Jumlah  : 5
# Total   : Rp 17500
# Bayar   : Rp 20000
# Kembali : Rp 2500
# ================================