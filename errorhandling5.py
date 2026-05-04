class InvalidAgeError(Exception):
    pass

class InvalidPriceError(Exception):
    pass

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Age {age} is not valid. Must be between 0-120.")
    return age

def set_price(price):
    if price < 0:
        raise InvalidPriceError(f"Price cannot be negative: {price}")
    return price

# Try

try:
    set_age(150)
except InvalidAgeError as e:
    print(f"Age Error: {e}")

try:
    set_price(-5000)
except InvalidPriceError as e:
    print(f"Price error : {e}")
    
# class InvalidAgeError(Exception) artinya buat class baru yang mewarisi semua perilaku Exception. pass karena kita tidak perlu tambah apa-apa — nama yang spesifik sudah cukup.
