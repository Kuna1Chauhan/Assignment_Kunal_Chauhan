import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
data = pd.read_excel("https://github.com/Kuna1Chauhan/EDA/raw/main/output.xlsx")

# Get all Pokemons whose spawn rate is less than 5%
spawn_rate_less_than_5 = data[data["spawn_chance"] < 5]
print("Pokemons with spawn rate less than 5%:")
print(spawn_rate_less_than_5)

# Plot the spawn rate distribution
plt.hist(data["spawn_chance"], bins=10)
plt.xlabel("Spawn Rate")
plt.ylabel("Count")
plt.title("Distribution of Spawn Rate")
plt.show()

# Get all Pokemons that have less than 4 weaknesses
less_than_4_weaknesses = data[data["weakness"].str.len() < 4]
print("Pokemons with less than 4 weaknesses:")
print(less_than_4_weaknesses)

# Plot the number of weaknesses distribution
weakness_counts = data["weakness"].str.len()
plt.hist(weakness_counts, bins=range(0, 11))
plt.xlabel("Number of Weaknesses")
plt.ylabel("Count")
plt.title("Distribution of Number of Weaknesses")
plt.show()

# Get all Pokemons that have no multipliers at all
no_multipliers = data[data["multipliers"].isna()]
print("Pokemons with no multipliers:")
print(no_multipliers)

# Get all Pokemons that do not have more than 2 evolutions
less_than_2_evolutions = data[data["next_evolution"].str.len() <= 2]
print("Pokemons with less than 2 evolutions:")
print(less_than_2_evolutions)

# Get all Pokemons whose spawn time is less than 300 seconds
data["spawn_time_minutes"] = pd.to_datetime(data["spawn_time"], format="%M:%S").dt.minute
spawn_time_less_than_300 = data[data["spawn_time_minutes"] < 5]
print("Pokemons with spawn time less than 300 seconds:")
print(spawn_time_less_than_300)

# Plot the spawn time distribution
plt.hist(data["spawn_time_minutes"], bins=10)
plt.xlabel("Spawn Time (minutes)")
plt.ylabel("Count")
plt.title("Distribution of Spawn Time")
plt.show()

# Get all Pokemon who have more than two types of capabilities
more_than_2_types = data[data["type"].str.len() > 2]
print("Pokemons with more than 2 types:")
print(more_than_2_types)

# Plot the number of types distribution
type_counts = data["type"].str.len()
plt.hist(type_counts, bins=range(0, 8))
plt.xlabel("Number of Types")
plt.ylabel("Count")
plt.title("Distribution of Number of Types")
plt.show()
