import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv("https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD")

# Get all the cars and their types that do not qualify for clean alternative fuel vehicle
not_clean_fuel = data[data["Clean Alternative Fuel Vehicle (CAFV)"] == "No"]
print("Cars and their types that do not qualify for clean alternative fuel vehicle:")
print(not_clean_fuel[["Model", "Type"]])

# Get all TESLA cars with the model year, and model type made in Bothell City
tesla_bothell = data[(data["Make"] == "TESLA") & (data["City"] == "BOTHELL")]
print("TESLA cars with the model year, and model type made in Bothell City:")
print(tesla_bothell[["Model Year", "Model"]])

# Get all the cars that have an electric range of more than 100, and were made after 2015
electric_range_100 = data[(data["Electric Range (Battery Only)"] > 100) & (data["Model Year"] > 2015)]
print("Cars with an electric range of more than 100, and were made after 2015:")
print(electric_range_100)

# Plot the distribution between city and electric vehicle type
plt.figure(figsize=(10, 6))
city_ev_type_counts = data.groupby(["City", "Electric Vehicle Type"]).size().unstack()
city_ev_type_counts.plot(kind="bar", stacked=True)
plt.xlabel("City")
plt.ylabel("Count")
plt.title("Distribution between City and Electric Vehicle Type")
plt.legend(title="Electric Vehicle Type")
plt.show()
