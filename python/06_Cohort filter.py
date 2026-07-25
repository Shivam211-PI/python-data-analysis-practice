def fiilter_patients():
   
    patients = [
    {"id": 1, "age": 45, "bmi": 31},
    {"id": 2, "age": 32, "bmi": 24},
    {"id": 3, "age": 50, "bmi": 29},
    {"id": 4, "age": 27, "bmi": 22},
    {"id": 5, "age": 60, "bmi": 34},
    {"id": 6, "age": 38, "bmi": 26}
    ]
    for patient in patients:
        if patient["bmi"] >=30:
            print(f"Patient ID: {patient['id']} ,Patient Age: {patient['age']}, patient BMI {patient['bmi']} is obese")
   
fiilter_patients()
