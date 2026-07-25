import numpy as np

conc = np.array(
    [1.2, 3.5, 2.8, 4.1, 0.9, 3.3]
    )

mean = np.mean(conc)
std_1 = np.std(conc)
median = np.median(conc)
indexing = np.argsort(conc)
ind_max = np.argmax(conc)

print("Mean:", round(mean,2))
print("Standard Deviation:", round(std_1,2))
print("Median:", median)
print("Indexing:", indexing)
print("Index of Maxium value:", ind_max)
