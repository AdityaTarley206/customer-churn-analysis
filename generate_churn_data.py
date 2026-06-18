import pandas as pd
import numpy as np
import random
import os

print("Generating 20,000+ customer records for churn analysis...")

# Set random seed
np.random.seed(42)
random.seed(42)

num_records = 21500

# Demographics
customer_ids = [f'CUST-{100000 + i}' for i in range(num_records)]
genders = [random.choice(['Male', 'Female']) for _ in range(num_records)]
senior_citizen = [random.choices([0, 1], weights=[0.85, 0.15])[0] for _ in range(num_records)]
partner = [random.choice(['Yes', 'No']) for _ in range(num_records)]
dependents = [random.choice(['Yes', 'No']) for _ in range(num_records)]

# Account Information
tenure = [random.randint(0, 72) for _ in range(num_records)]
contract_types = ['Month-to-month', 'One year', 'Two year']
# Higher tenure -> more likely to be on a longer contract
contracts = []
for t in tenure:
    if t < 12:
        contracts.append(random.choices(contract_types, weights=[0.8, 0.15, 0.05])[0])
    elif t < 36:
        contracts.append(random.choices(contract_types, weights=[0.4, 0.4, 0.2])[0])
    else:
        contracts.append(random.choices(contract_types, weights=[0.1, 0.3, 0.6])[0])

paperless_billing = [random.choice(['Yes', 'No']) for _ in range(num_records)]
payment_methods = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
payment_method = [random.choice(payment_methods) for _ in range(num_records)]

# Services
monthly_charges = []
total_charges = []
churn = []

for i in range(num_records):
    # Base charge
    base_charge = random.uniform(20.0, 120.0)
    monthly_charges.append(round(base_charge, 2))
    
    # Calculate Total Charges based on tenure (with some noise)
    if tenure[i] == 0:
        total_charges.append(round(base_charge, 2))
    else:
        total = base_charge * tenure[i] * random.uniform(0.9, 1.1)
        total_charges.append(round(total, 2))
        
    # Introduce some logic for churn
    churn_prob = 0.15  # Base probability
    
    if contracts[i] == 'Month-to-month':
        churn_prob += 0.20
    if monthly_charges[-1] > 80:
        churn_prob += 0.10
    if tenure[i] < 6:
        churn_prob += 0.15
    if senior_citizen[i] == 1:
        churn_prob += 0.05
    if partner[i] == 'Yes' and dependents[i] == 'Yes':
        churn_prob -= 0.10
        
    churn_prob = max(0.01, min(0.99, churn_prob))
    
    is_churn = 'Yes' if random.random() < churn_prob else 'No'
    churn.append(is_churn)

# Build DataFrame
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Gender': genders,
    'SeniorCitizen': senior_citizen,
    'Partner': partner,
    'Dependents': dependents,
    'Tenure': tenure,
    'Contract': contracts,
    'PaperlessBilling': paperless_billing,
    'PaymentMethod': payment_method,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'Churn': churn
})

# Add a few missing values in TotalCharges to simulate real-world data
missing_indices = random.sample(range(num_records), 50)
for idx in missing_indices:
    df.loc[idx, 'TotalCharges'] = np.nan

output_path = 'customer_data.csv'
df.to_csv(output_path, index=False)

print(f"Successfully generated {len(df)} records!")
print(f"Data saved to {os.path.abspath(output_path)}")
