import pandas as pd
import numpy as np

# load data
data = pd.read_csv(r"C:\Users\pinoy\Desktop\Coding\healthcare-app\data\FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")

# normalize and clean up data
data.columns = data.columns.str.lower().str.replace(' ', '_') # columns to snake_case

data.replace(["N/A", "Too Few to Report"], np.nan, inplace=True) # replace N/A and "Too Few to Report" with NaN
# convert numeric columns to their proper types
numeric_cols = [
    'number_of_discharges', 'excess_readmission_ratio', 
    'predicted_readmission_rate', 'expected_readmission_rate', 
    'number_of_readmissions'
]
data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')
# convert date columns to datetime
data["start_date"] = pd.to_datetime(data["start_date"]) 
data["end_date"] = pd.to_datetime(data["end_date"])

# adding additional data for analysis
data["actual_readmission_rate"] = ((data["number_of_readmissions"] / data["number_of_discharges"]) * 100).round(4)

# export cleaned data (for double checking)
data.to_csv(r"C:\Users\pinoy\Desktop\Coding\healthcare-app\data\cleaned_up_data.csv", index=False)