try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")

except ValueError:
    print("That's not a valid number!")

except ZeroDivisionError:
    print("Can't divide by zero!")

finally:
    print("Program finished.")   # selalu tercetak, error atau tidak

# finally biasa dipakai untuk cleanup — tutup file, tutup koneksi database, apapun yang harus selalu dijalankan.
