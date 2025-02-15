import restaurant

# Create an order with some items
order = restaurant.Order([restaurant.cocaCola, restaurant.nachos, restaurant.beefSteak], table_number=1)

order.display_order_details()

# -------------------------------------------------

print("\nOrder Items:")

# Iterate through items and access their attributes
for item in order:
    print(f"Item: {item.name}, Price: {item.price}")
    if isinstance(item, restaurant.Beverage):
        print(f"Volume: {item.volume}ml")
    elif isinstance(item, restaurant.Appetizer):
        print(f"Recommended Dip: {item.recommended_dip}")
