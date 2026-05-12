try:
    number = int("abc")

except ValueError as e:
    print(f"Error caught: {e}")

# as e menyimpan detail error ke variabel e — berguna untuk debugging.
