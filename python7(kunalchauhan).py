import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv("https://github.com/Kuna1Chauhan/EDA/raw/main/output.csv")

# Get all the Earth meteorites that fell before the year 2000
before_2000 = data[data["year"] < 2000]
print("Earth meteorites fell before the year 2000:")
print(before_2000)

# Plot the distribution of meteorite falls by year
plt.hist(data["year"], bins=range(1800, 2023, 10))
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Distribution of Meteorite Falls by Year")
plt.show()

# Get all the earth meteorites coordinates that fell before the year 1970
before_1970 = data[data["year"] < 1970]
print("Earth meteorites fell before the year 1970:")
print(before_1970)

# Plot the distribution of meteorite falls by year for the before 1970 subset
plt.hist(before_1970["year"], bins=range(1800, 1971, 10))
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Distribution of Meteorite Falls before 1970")
plt.show()

# Assuming mass is in kg, get all the earth meteorites whose mass was more than 10000kg
mass_more_than_10000 = data[data["mass"] > 10000]
print("Earth meteorites with mass more than 10000kg:")
print(mass_more_than_10000)

# Plot the distribution of meteorite masses
plt.hist(data["mass"], bins=range(0, int(data["mass"].max()) + 5000, 5000))
plt.xlabel("Mass (kg)")
plt.ylabel("Count")
plt.title("Distribution of Meteorite Masses")
plt.show()
