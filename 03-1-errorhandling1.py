
# anatomy try/except

try:
    number = int(input("Enter a number :"))
    result = 10 / number
    print(f"Result: {result}")

except ValueError:
    print("That's not a valid number!")

except ZeroDivisionError:
    print("Cannot divided by zero")

# Python coba jalankan blok try. Kalau gagal, ia lihat errornya cocok dengan except yang mana, lalu lompat ke sana. Sisa kode di try dilewati.
