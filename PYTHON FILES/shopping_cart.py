catalog = {
    "banana": 5000,
    "apple": 3000,
    "orange": 4000,
    "grape": 6000,
    "rice": 1000
}
1
cart = []

print("Welcome to the Fruit Store!")
print("Available products:")
for item, price in catalog.items():
    print(f"{item.title()} : ${price}")

while True:
    print("\n--Menu---")
    print("1. Add to Cart") 
    print("2. Remove from Cart")
    print("3. View Cart")
    print("4. Checkout & Exit")

    choice = input("Choose an option 1-4: ")
    if choice == "1":
        item = input("Enter product name: ").lower()
        if item in catalog:
            cart.append(item)
            print(f"{item.title()} added to cart")
        else:
            print("Item not found")

    elif choice == "2":
        item = input("Enter product name to remove: ").lower()
        if item in cart:
            cart.remove(item)
            print(f"{item.title()} removed from the cart")
        else:
            print("Item not found in cart")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            total = 0
            for item in cart:
                price = catalog[item]
                print(f"{item.title()} : ${price}")
                total += price
            print(f"Total: ${total}")

    elif choice == "4":
        print("\n---Checkout---")
        if not cart:
            print("NOTHING TO CHECKOUT")
        else:
            total = sum([catalog[item] for item in cart])
            print("Items purchased:")
            for item in cart:
                print(f"{item.title()} : ${catalog[item]}")
            print(f"Total Amount to Pay: ${total}")
            print("Thank you for shopping with us!")
        break

    else:
        print("Invalid choice, please choose from 1-4")







