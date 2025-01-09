# format specifiers = {value:flags} format a value based on what flags are inserted
# NOTE -> We can also mix match the operators

# .(number)f = round to that many decimal places (fixed point)
# :(number)  = allocate that many spaces
# :03 = allocate and zero pad that many spaces -> v age je space bch rhi tn 0 lga denge
# :<  = left justify
# :>  = right justify
# :^  = center align
# :+  = use a plus sign to indicate positive value (and - for negative)
# :=  = place sign to leftmost position
# :   = insert a space before positive numbers
# :,  = comma seperator

price1 = 3.141
price2 = -987.65
price3 = 1000000000.000

print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price1:10}")
print(f"Price 1 is ${price1:09}")
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price1:^10}")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 1 is ${price1:=10}")
print(f"Price 2 is ${price2:=10}")
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3:,}")
print()
print(f"Price 3 is ${price3:+,.2f}")

