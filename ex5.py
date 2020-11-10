name = 'Cem Yeniceli'
age = 33
height_in_cm = 190
height_in_inches = 0.393700787 * height_in_cm
weight_in_kg = 86
weight_in_pounds = weight_in_kg * 2.20462262
eyes = 'Hazel'
teeth = 'White'
hair = 'Blonde'

print(f"Let's talk about {name}.")
print(f"He's {height_in_cm} cm tall.")
print(f"He's {height_in_inches} inches tall.")
print(f"He's {weight_in_kg} kg heavy.")
print(f"He's {weight_in_pounds} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height_in_cm + weight_in_kg
print(f"If I add age, height_in_cm and weight_in_kg I get {total}.")