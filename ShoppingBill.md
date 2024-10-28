# Assignment: Python Functions - Shopping Bill Calculator

### Objective:
- Use various types of Python functions to build a flexible shopping bill calculator. Your solution should make use of positional-only arguments, keyword-only arguments, variable-length arguments, and both required and default parameters.
---
# Tasks
### Task 1: Define a Function to Add Items to the Shopping Bill
- Create a function called add_item that:
- Accepts the following parameters:
 - item_name (str)
 - price (float)
 - quantity (int, optional, defaults to 1)
- This function should print a message indicating that the item has been added to the bill.

```python
add_item("Apples", 1.5, 4)
```
Expected Output
```
Added 4 Apples at $1.5 each to the shopping bill.
```
### Task 2: Define a Function to Set Discounts for Individual Items
- Create a function called set_discount that:

- Uses a keyword argument for the item name and a required positional argument for the discount percentage.
- This function should print a message indicating the discount set for the item.

```python
set_discount(item_name="Apples", discount=10)
```
Expected Output
```css
Set a 10% discount for Apples.
```
### Task 3: Define a Function to Calculate the Total Bill
- Create a function called calculate_total that:

- Takes a list of item prices and quantities as parameters.
- The function should loop through the items, calculating the total cost of the items added based on the provided prices and quantities.
- It should print the total amount before discounts.

```python
calculate_total([1.5, 2.0, 1.2], [4, 1, 2])
```
Expected Output
```bash
Total amount before discounts: $10.4
```

### Task 4: Define a Function to Generate and Display the Bill
- Create a function called generate_bill that:

- Takes bill_id as a positional-only argument.
- Requires date and cashier as keyword-only arguments, with cashier defaulting to "Admin".
- This function should print a formatted bill summary including:
- The bill_id, date, and cashier.
- Total amount before discounts.

```python
generate_bill(123, date="2024-11-05", cashier="John")
```
Expected Output
```yaml
Bill ID: 123
Date: 2024-11-05
Cashier: John
Total amount before discounts: $10.4
```

## Notes
- For add_item, focus on printing a message rather than storing data.
- For set_discount, assume a simple implementation that only prints the discount.
- For calculate_total, ensure to loop through the item prices and quantities stored in arrays to calculate the total.
- Ensure generate_bill combines the output of the previous tasks and presents it clearly.
