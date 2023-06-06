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

    # Extract the required attributes from the data and create a DataFrame
    pokemon_list = []
    for pokemon in data["pokemon"]:
        multipliers = pokemon.get("multipliers", [])
        multipliers_str = ", ".join(map(str, multipliers)) if multipliers is not None else ""
        weaknesses = pokemon.get("weaknesses", [])
        weaknesses_str = ", ".join(weaknesses) if weaknesses is not None else ""
        pokemon_data = {
            "id": pokemon["id"],
            "num": pokemon["num"],
            "name": pokemon["name"],
            "img": pokemon["img"],
            "type": ", ".join(pokemon["type"]),
            "height": pokemon["height"],
            "weight": pokemon["weight"],
            "candy": pokemon.get("candy", ""),
            "candy_count": pokemon.get("candy_count", ""),
            "egg": pokemon.get("egg", ""),
            "spawn_chance": pokemon.get("spawn_chance", ""),
            "avg_spawns": pokemon.get("avg_spawns", ""),
            "spawn_time": pokemon.get("spawn_time", ""),
            "multipliers": multipliers_str,
            "weakness": weaknesses_str
        }
        pokemon_list.append(pokemon_data)
    df = pd.DataFrame(pokemon_list)

    # Save the data to an Excel file
    df.to_excel(output_file, index=False)
    print("Data conversion completed. Saved to", output_file)

# Example usage
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
output_file = "output.xlsx"
download_and_convert_data(url, output_file)


