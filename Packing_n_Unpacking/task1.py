# Task 1 customer order processing
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Travis", "Tv", 3),
    ("Abe", "Xbox", 2)
]

def list_of_orders(orders):
    '''Print the list of orders in a user friendly format.'''
    for customer, item, quantity in orders:
        if quantity > 1:
            print(f"Hi there, {customer}. you have ordered {quantity} {item}'s.")
        else:
            print(f"Hi there, {customer}. you have ordered {quantity} {item}.")

list_of_orders(orders)
