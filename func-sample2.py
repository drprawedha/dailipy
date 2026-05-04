
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

def print_receipt(items,paid):
    print("============================")
    print('       STRUK BELANJA')
    print("============================")

    grand_total = 0
    for item in items:
        total = calculate_total(item['price'],item['qty'],item['discount'])
        grand_total += total
        print(f"Item  : {item['name']}")
        print(f"Price   : Rp {item['price']}")
        print(f"Qty     : {item['qty']}")
        print(f"Total   : Rp {total}")
        print("============================")

    change = calculate_change(grand_total, paid)
    print(f"Grand Total : Rp {grand_total}")
    print(f"Paid        : Rp {paid}")
    if change == -1:
        print(f"Amount due  : Rp {grand_total - paid}")
    else:
        print(f"Change      : Rp {change}")
    print("=============================")


# Error Handling
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Valeu cannot be negative")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Try Again")

def get_float_input(prompt, min_val=0, max_val=1):
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                raise ValueError(f"Must be between {min_val} and {max_val}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

# Error Handling 

def add_item():
    name    = input("Item Name : ")
    price   = get_int_input("Price :")
    qty     = get_int_input("Qty :")
    discount = get_float_input("Discount (0-1): ")
    return {
        "name": name, 
        "price": price, 
        "qty":qty,
        "discount":discount}

# --- main program ---
items = []

while True:
    print("\n1. Add Transaction")
    print("2. Print Receipt ")
    choice = input("Option: ")

    if choice == "1":
        items.append(add_item())
    elif choice == "2":
        # hitung dulu grand total
        grand_total = sum(calculate_total(item['price'], item['qty'], item['discount']) for item in items)
        print(f"\nGrand Total : Rp {grand_total}")
        paid = get_int_input("Paid: ")
        print_receipt(items, paid)
        break
    else:
        print("Option is not valid.")

