import numpy as np

conc = np.array(
    [1.2, 3.5, 2.8, 4.1, 0.9, 3.3]
    )

mcg_ml = np.round(conc * 1000, 0)
print("Con.in mcg/ml:", mcg_ml)