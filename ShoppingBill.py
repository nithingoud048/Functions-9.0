# Write Your Code Here
# shoppingbill.py

def add_item(item_name: str, price: float, quantity: int = 1):
    """Adds an item to the shopping bill."""
    print(f"Added {quantity} {item_name} at ${price} each to the shopping bill.")

def set_discount(*, item_name: str, discount: float):
    """Sets a discount for an individual item."""
    print(f"Set a {discount}% discount for {item_name}.")

def calculate_total(prices: list, quantities: list) -> float:
    """Calculates the total amount before discounts."""
    total = 0
    for price, quantity in zip(prices, quantities):
        total += price * quantity
    print(f"Total amount before discounts: ${total:.2f}")
    return total

def generate_bill(bill_id: int, *, date: str, cashier: str = "Admin"):
    """Generates and displays the bill summary."""
    # Calculate a sample total for the bill (this can be adjusted based on actual item inputs)
    total_amount = calculate_total([1.5, 2.0, 1.2], [4, 1, 2])
    
    print(f"Bill ID: {bill_id}")
    print(f"Date: {date}")
    print(f"Cashier: {cashier}")
    print(f"Total amount before discounts: ${total_amount:.2f}")

# Example usage
if __name__ == "__main__":
    add_item("Apples", 1.5, 4)
    set_discount(item_name="Apples", discount=10)
    calculate_total([1.5, 2.0, 1.2], [4, 1, 2])
    generate_bill(123, date="2024-11-05", cashier="John")
