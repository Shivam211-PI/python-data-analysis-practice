import numpy as np 

age = np.array([5,8,10,14,17,18,20,26,36,49,60,70,85])

separate = np.where((age<18), 
                    "minor", 
                    np.where((age<60), 
                             "adult", "senior"))
print(separate)