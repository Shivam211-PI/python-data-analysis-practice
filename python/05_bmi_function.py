#Write def bmi(weight_kg, height_m): that returns BMI rounded to 1 decimal, and handles the case where
#height is 0 (avoid divide-by-zero). Test with 3 patients.

def bmi(weight_kg, height_m):
    if height_m == 0:
        return "Height cannot be zero."
    bmi_value = weight_kg / (height_m ** 2)
    return round(bmi_value, 1)

# Test with 3 patients
print(bmi(70, 1.75))  # Expected: 22.9
print(bmi(80, 1.80))  # Expected: 24.7
print(bmi(60, 0))     # Expected: "Height cannot be zero."