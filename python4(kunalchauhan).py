import requests
import pandas as pd

def download_and_convert_data(url, output_file):
    # Download the data from the provided link
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to download the data.")
        return

    # Read the data as JSON
    data = response.json()

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Select the desired attributes
    selected_columns = ["name", "id", "nametype", "recclass", "mass (g)", "year", "reclat", "reclong"]
    df = df[selected_columns]

    # Rename the columns
    column_mapping = {
        "name": "Name of Earth Meteorite",
        "id": "ID of Earth Meteorite",
        "nametype": "Type of Earth Meteorite",
        "recclass": "Class of Earth Meteorite",
        "mass (g)": "Mass of Earth Meteorite",
        "year": "Year of Impact",
        "reclat": "Latitude",
        "reclong": "Longitude"
    }
    df = df.rename(columns=column_mapping)

    # Save the data as a CSV file
    df.to_csv(output_file, index=False)
    print("Data conversion completed. Saved to", output_file)


url = "https://data.nasa.gov/resource/y77d-th95.json"
output_file = "output.csv"
download_and_convert_data(url, output_file)
