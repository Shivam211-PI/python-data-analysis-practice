def filter_patients():

    patients = [
        {"id": 1, "age": 45, "bmi": 31},
        {"id": 2, "age": 32, "bmi": 24},
        {"id": 3, "age": 50, "bmi": 29},
        {"id": 4, "age": 27, "bmi": 22},
        {"id": 5, "age": 60, "bmi": 34},
        {"id": 6, "age": 38, "bmi": 26}
    ]

    obese = []
    not_obese = []

    for patient in patients:
        if patient["bmi"] >= 30:
            obese.append(patient)
        else:
            not_obese.append(patient)

    return obese, not_obese


obese_patients, non_obese_patients = filter_patients()

print("Obese Patients:")
for patient in obese_patients:
    print(patient)

print("\nNon-Obese Patients:")
for patient in non_obese_patients:
    print(patient)