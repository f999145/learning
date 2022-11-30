# Decimals

# Set the Result to a variable:
a = 1/3
# Format the result :.3f is the length of the digits "AFTER" the decial point.
print(f"{a:.3f}")
# Returns: 0.333

print(f"{a:.6f}")
# Returns: 0.333333

print(f"{a:.32f}")
# Returns: 0.33333333333333331482961625624739

print(f"{a:.50f}")
# Returns: 0.33333333333333331482961625624739099293947219848633

print(f"{a:.55f}")
# Returns: 0.3333333333333333148296162562473909929394721984863281250

# # NOTE: this does round see the difference between the ending of .50 & .55

# Digits & Decimals

# You can do the same for leading zeros:
a = (1/3) + 145630

print(f"{a:016.03f}")

# Returns 000000145630.333

# if you don't want to lead with Zeros and just spaces.
print(f"{a:16.03f}")
# Returns "      145630.333"
# # NOTE: 
# With this one - notice there are only 12 Digits/Spaces Left of the decimal.

print(f"{a:016.55f}")
# Returns 145630.3333333333430346101522445678710937500000000000000000000
# # NOTE:
# will never show leading spaces or zeros
# as the decimal digit count is greater than the total digit count.

# So the way to calculate it what will properly be displayed is:
# `f"{VARIABLE:(TOTALDIGITS).(DECIMALDIGITS)f}"`
# Total Digits - Decimal Digits - 1 (for the decimal point)
# If the return from the equasion above is < 1 
# # There will never be a leading digit/space.  
# As shown in the last example of Digits & Decimals.  (16-55-1) =
# "-40"  So no Leading digits will ever show.

# Digits Only

# If you only need to update formats for Digits and no Decimals:
a = 148
print(f"{a:016d}")
# or
print(f"{a:016.0f}")

# Returns 0000000000000148

print(f"{a:16d}")
# or 
print(f"{a:16.0f}")
# Returns "             148"

# Exceptions to Note:

a = 148.15
print(f"{a:16d}")  # THROWS AN ERROR:
# ValueError: Unknown format code 'd' for object of type 'float'

# or 
print(f"{a:16.0f}")
# Returns "             148"
# # NOTE: This TRUNCATES YOUR DECIMAL FORMAT.
