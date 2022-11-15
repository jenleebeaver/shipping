weight = 4.8 
drone_weight = 1.5

# Ground Shipping 
if weight <= 2:
  cost = (1.5 * weight) + 20;
  print(cost);
elif weight > 2 and weight <= 6:
  cost = (3 * weight) + 20;
  print(cost);
elif weight > 6 and weight <= 10:
  cost = (4 * weight) + 20;
  print(cost);
else:
  cost = (4.75 * weight) + 20;
  print(cost);

# Ground Shipping Premium 
if weight > 0:
  cost = 125.00
  print(cost)

# Drone Shipping 
if weight <= 2:
  cost = (4.5 * weight);
  print(cost);
elif weight > 2 and weight <= 6:
  cost = (9 * weight);
  print(cost);
elif weight > 6 and weight <= 10:
  cost = (12 * weight);
  print(cost);
else:
  cost = (14.25 * weight);
  print(cost);

# Drone Shipping w/ drone weight
# if drone_weight <= 2:
#   cost = (4.5 * drone_weight);
#   print(cost);
# elif drone_weight > 2 and drone_weight <= 6:
#   cost = (9 * drone_weight);
#   print(cost);
# elif drone_weight > 6 and drone_weight <= 10:
#   cost = (12 * drone_weight);
#   print(cost);
# else:
#   cost = (14.25 * drone_weight);
#   print(cost);
