# 1. Variables para sa Inputs (Galing sa User)
item_name = input("Ano ang binibili mo? ")
price = float(input("Magkano ang presyo (₱)? "))
quantity = int(input("Ilan ang bibilhin mo? "))

# 2. Math Calculations gamit ang Variables
subtotal = price * quantity
discount = subtotal * 0.10  # Fixed 10% discount
total_price = subtotal - discount

# 3. Pag-display ng Output / Receipt
print("\n--- RECEIPT ---")
print(f"Item: {item_name}")
print(f"Dami: {quantity} pcs")
print(f"Subtotal: ₱{subtotal}")
print(f"Discount (10%): -₱{discount}")
print(f"Total na Babayaran: ₱{total_price}")
