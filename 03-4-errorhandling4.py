try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid Input! \nPlease only put a number")

else:
    print(f"Success! You entered {number}")

finally:
    print("Done")