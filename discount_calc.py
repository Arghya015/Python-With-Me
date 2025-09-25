# Create the fee and discount_percent variables
fee = 1536
discount_percent = 10

# Compute discount and assign it to the discount variable
discount = (discount_percent/100)*fee

# Compute and print the fee you have to pay
final = fee-discount
print(final)
