import numpy as np

conc = np.array(
    [1.2, 3.5, 2.8, 4.1, 0.9, 3.3]
    )

msk = conc > 3.0
sm = np.sum(msk)
print("Bollean mask:", msk)
print("Total value grater than 3.0 is ",sm)
