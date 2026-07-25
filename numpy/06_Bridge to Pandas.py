import numpy as np 
import pandas as pd

read = pd.read_csv(r"D:\New python\practise claude\practisee\pandas data sets\diabetes.csv")
print(read)

# Load only the Age column
age = np.genfromtxt(
    r"D:\New python\practise claude\practisee\pandas data sets\diabetes.csv",
    delimiter=",",
    skip_header=1,
    usecols=7
)

# Calculate mean age
mean_age = np.mean(age)

print("Age column:")
print(age)

print(f"\nMean Age: {mean_age:.2f}")