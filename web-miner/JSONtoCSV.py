# Created by Sam Tucker Dec 4 2024
import os
import json
import pandas as pd

current_directory = os.getcwd()

csv_headers = [
    "Property Price", "Street Address", "City", "State", "Zipcode", "Bedrooms", "Bathrooms" , "Home Type", "Home Status", "Living Area"
]

output_csv = 'new_york_properties.csv'

property_list = []

for filename in os.listdir(current_directory):
    if filename.endswith(".json"):
        filepath = os.path.join(current_directory, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            listings = data.get("cat1", {}).get("searchResults", {}).get("listResults", [])
            for listing in listings:
                homeinfo = listing.get("hdpData", {}).get("homeInfo", {})
                price = homeinfo.get("price")
                street_address = homeinfo.get("streetAddress")
                city = homeinfo.get("city")
                state = homeinfo.get("state")
                zipcode = homeinfo.get("zipcode")
                bedrooms = homeinfo.get("bedrooms")
                bathrooms = homeinfo.get("bathrooms")
                home_type = homeinfo.get("homeType")
                home_status = homeinfo.get("homeStatus")
                living_area = homeinfo.get("livingArea")

                if all([price, street_address, city, state, zipcode, bedrooms, bathrooms, home_type, home_status, living_area]):
                    property_list.append([price, street_address, city, state, zipcode, bedrooms, bathrooms, home_type, home_status, living_area])

df = pd.DataFrame(property_list, columns=csv_headers)
df.to_csv(output_csv, index=False)

print(f"CSV file created: {output_csv}")
