drug_name = input("Enter the drug name: ").lower()

dict = {"amoxicilin": 500,
        "paracetamol": 650,
        "ibuprofen" : 400}

if drug_name in dict:
    dose = dict[drug_name]
    print(f"The recommended dose of {drug_name} is {dose} mg.")

else:
    print(f"Sorry, we do not have information on {drug_name}.")
    