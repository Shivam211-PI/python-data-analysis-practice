daily_dose = [400,900,650,1200,300]

max_safe = 800 
print(f"There is total of {len(daily_dose)} drugs doses")
for i in range(len(daily_dose)):
    if daily_dose[i] > max_safe:
        print(f"Your dose {daily_dose[i]} mg is not in safe range")
    else:
        print(f"Your dose {daily_dose[i]} mg is in safe range")
# count the number of doses that are above the safe limit
count_above_safe = 0
for i in range(len(daily_dose)):
    if daily_dose[i] > max_safe:
        count_above_safe += 1

print(f"Number of doses above safe limit: {count_above_safe}")
