import numpy as np

patients = np.array([
    [10, 12, 15],          #PATIENT 1
    [20, 22, 25],          #PATIENT 2
    [30, 32, 35],          #PATIENT 3
    [40, 42, 45]           #PATIENT 4
])

print(patients)

mean = np.mean(patients, axis = 0)
mean1 = np.mean(patients, axis = 1)

print("Mean of each column:", mean)
print("Mean of each row:", np.round(mean1,2))

