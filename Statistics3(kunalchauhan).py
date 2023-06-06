import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load the dataset
data_url = "https://raw.githubusercontent.com/Kuna1Chauhan/EDA/main/BP%20data.csv"
df = pd.read_csv(data_url)

# Extract the relevant columns
bp_before = df.iloc[:,[1]]
bp_after = df.iloc[:,[2]]

# a. Measure the dispersion and interpret the results
dispersion_bp_before = np.var(bp_before)
dispersion_bp_after = np.var(bp_after)
print("Dispersion in Blood Pressure Before:", dispersion_bp_before)
print("Dispersion in Blood Pressure After:", dispersion_bp_after)
# Interpretation: The dispersion measures (variance) indicate the spread or variability of the blood pressure values before and after. Higher dispersion indicates greater variability in the measurements.

# b. Calculate mean and 5% confidence interval and plot it in a graph
mean_bp_before = np.mean(bp_before)
mean_bp_after = np.mean(bp_after)
confidence_interval_bp_before = stats.t.interval(0.95, len(bp_before)-1, loc=mean_bp_before, scale=stats.sem(bp_before))
confidence_interval_bp_after = stats.t.interval(0.95, len(bp_after)-1, loc=mean_bp_after, scale=stats.sem(bp_after))

print("Mean Blood Pressure Before:", mean_bp_before)
print("Mean Blood Pressure After:", mean_bp_after)
print("Confidence Interval for Blood Pressure Before:", confidence_interval_bp_before)
print("Confidence Interval for Blood Pressure After:", confidence_interval_bp_after)

# Plotting the means and confidence intervals
labels = ['Before', 'After']
means = [mean_bp_before, mean_bp_after]
confidence_intervals = [confidence_interval_bp_before, confidence_interval_bp_after]
errors = [ci[1] - mean for ci, mean in zip(confidence_intervals, means)]

plt.bar(labels, means, yerr=errors, capsize=10)
plt.ylabel('Mean Blood Pressure (mmHg)')
plt.title('Mean Blood Pressure Before and After')

plt.show()

# c. Calculate Mean Absolute Deviation (MAD) and Standard Deviation (SD) and interpret the results
mad_before = np.mean(np.abs(bp_before - np.mean(bp_before)))
mad_after = np.mean(np.abs(bp_after - np.mean(bp_after)))

std_before = np.std(bp_before)
std_after = np.std(bp_after)

print("Mean Absolute Deviation (MAD) of Blood Pressure Before: {:.2f}".format(mad_before.item()))
print("Mean Absolute Deviation (MAD) of Blood Pressure After: {:.2f}".format(mad_after.item()))
print("Standard Deviation (SD) of Blood Pressure Before: {:.2f}".format(std_before.item()))
print("Standard Deviation (SD) of Blood Pressure After: {:.2f}".format(std_after.item()))

# d. Calculate the correlation coefficient and check the significance at 1% level of significance
correlation_coefficient, p_value = stats.pearsonr(bp_before, bp_after)
significance_level = 0.01

print("Correlation Coefficient: {:.2f}".format(correlation_coefficient.item()))
if p_value < significance_level:
    print("The correlation is significant at the 1% level of significance.")
else:
    print("The correlation is not significant at the 1% level of significance.")