import pandas as pd
from scipy.stats import shapiro

# Read the data from the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/Kuna1Chauhan/EDA/main/BP%20data.csv')

# Extract the 'Blood Pressure Before (mmHg)' and 'Blood Pressure After (mmHg)' columns
bp_before = df.iloc[:,[1]]
bp_after = df.iloc[:,[2]]

# Perform the Shapiro-Wilk test on the 'Blood Pressure After' data
statistic, p_value = shapiro(bp_after)

# Print the test results
print("Shapiro-Wilk test results:")
print("Statistic:", statistic)
print("p-value:", p_value)

# Interpret the results
alpha = 0.05  # Set the significance level
if p_value > alpha:
    print("The p-value is greater than the significance level, so we do not reject the null hypothesis.")
    print("The change in blood pressure approximately follows a normal distribution.")
else:
    print("The p-value is less than or equal to the significance level, so we reject the null hypothesis.")
    print("The change in blood pressure does not follow a normal distribution.")
