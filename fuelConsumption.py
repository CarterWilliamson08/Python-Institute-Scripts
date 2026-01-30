CONSTANT = 235.214583  # derived conversion factor

def liters_100km_to_miles_gallon(liters):
    return CONSTANT / liters


def miles_gallon_to_liters_100km(miles):
    return CONSTANT / miles


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
