
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
        total = calculate_total(item['price'],item['qty'])
        grand_total += total
        print(f"Item  : {item['name']}")
        print(f"Price   : Rp {item['price']}")
        print(f"Qty     : {item['qty']}")
        print(f"Total   : Rp {total}")
        print("============================")

    change = calculate_change(grand_total, paid)
    print(f"Grand Total : Rp {grand_total}")
    print(f"Paid        : Rp {paid}")
    print(f"Change      : Rp {change}")
    print("=============================")

    if change == -1:
        print(f"Amount due : Rp {grand_total - paid}")
    else:
        print(f"Change     : Rp {change}")

def add_item():
    name    = input("Item Name : ")
    price   = int(input("Price :"))
    qty     = int(input("Qty :"))
    discount = float(input("Discount (0-1): "))
    return {
        "name": name, 
        "price": price, 
        "qty":qty,
        "discount":discount}

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
        paid = int(input("Paid: "))
        print_receipt(items, paid)
        break
    else:
        print("Option is not valid.")
