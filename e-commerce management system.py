# E-Commerce Management System

print("1. Mobile")
print("2. Laptop")
print("3. Headphones")

choice = int(input("Enter your choice: "))

if choice == 1:
    price = 15000
    quantity = int(input("Enter quantity: "))

    if quantity > 0:
        total = price * quantity
        print("Mobile selected")
        print("Total Price =", total)
    else:
        print("Invalid quantity")

elif choice == 2:
    price = 50000
    quantity = int(input("Enter quantity: "))

    if quantity > 0:
        total = price * quantity
        print("Laptop selected")
        print("Total Price =", total)
    else:
        print("Invalid quantity")

elif choice == 3:
    price = 2000
    quantity = int(input("Enter quantity: "))

    if quantity > 0:
        total = price * quantity
        print("Headphones selected")
        print("Total Price =", total)
    else:
        print("Invalid quantity")

else:
    print("Invalid choice!")

print("Thank you for shopping!")
