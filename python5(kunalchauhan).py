import requests

def download_and_extract_data(url):
    # Download the data from the provided API link
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to download the data.")
        return

    # Extract the desired data attributes
    data = response.json()
    show_id = data["id"]
    show_url = data["url"]
    show_name = data["name"]

    episodes = data["_embedded"]["episodes"]
    extracted_data = []

    for episode in episodes:
        episode_data = {
            "id": episode["id"],
            "url": episode["url"],
            "name": episode["name"],
            "season": episode["season"],
            "number": episode["number"],
            "type": episode["type"],
            "airdate": episode["airdate"],
            "airtime": episode["airtime"],
            "runtime": episode["runtime"],
            "average_rating": episode["rating"]["average"],
            "summary": episode["summary"].strip("<p>").strip("</p>"),
            "medium_image": episode["image"]["medium"],
            "original_image": episode["image"]["original"]
        }
        extracted_data.append(episode_data)

    # Display the extracted data
    for episode in extracted_data:
        print("Episode ID:", episode["id"])
        print("Episode URL:", episode["url"])
        print("Episode Name:", episode["name"])
        print("Season:", episode["season"])
        print("Episode Number:", episode["number"])
        print("Type:", episode["type"])
        print("Airdate:", episode["airdate"])
        print("Airtime:", episode["airtime"])
        print("Runtime:", episode["runtime"])
        print("Average Rating:", episode["average_rating"])
        print("Summary:", episode["summary"])
        print("Medium Image Link:", episode["medium_image"])
        print("Original Image Link:", episode["original_image"])
        print("-" * 30)


url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
download_and_extract_data(url)
