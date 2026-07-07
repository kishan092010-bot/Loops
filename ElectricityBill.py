# Program On Calculate Electricity Bill

# Step 2: Understand the price ranges

# Units Used Price per Unit Extra Tax (Surcharge)

# 0 – 49 ₹2.60 ₹25

# 50 – 100 ₹3.25 ₹35

# 101 – 200 ₹5.26 ₹45

# More than 200 ₹8.45 ₹75

# Step 3: First condition

# Simple meaning:

# If the customer used less than 50 units, every unit costs ₹2.60.

# Example: 40 units

# Calculation:

# amount = 40 × 2.60 = ₹104

# surcharge = ₹25

# total = 104 + 25 = ₹129

units = int(input("Enter the number of units consumed: "))
# Check the electricity slab
# Slab 1: Less than 50 units
if units < 50:
    amount = units * 2.60
    surcharge = 25

# Slab 2: 50 - 100 units
elif units <= 100:
    # First 50 units = 50 * 2.60 = 130
    # Remaining units = (units - 50) * 3.25
    amount = 130 + ((units - 50) * 3.25) 
    surcharge = 35

# a,b,c = b,c,a
# print(a,b,c)