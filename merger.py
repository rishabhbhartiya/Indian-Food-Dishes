import pandas as pd
import json
import os

# Load the CSV file
csv_file = '/Users/rishabhbhartiya/Desktop/INDIAN FOOD/CODE/INDIAN_FOOD_RECIPE_DATA.csv'
df = pd.read_csv(csv_file)

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Directory containing JSON files
json_dir = '/Users/rishabhbhartiya/Desktop/INDIAN FOOD/RECIPE_JSON'

# Iterate through JSON files and merge with CSV data
for index, row in df.iterrows():
    json_file = os.path.join(json_dir, f"{row['name']}.json")
    if os.path.exists(json_file):
        json_data = load_json(json_file)
        for key, value in json_data.items():
            df.at[index, key] = value

# Save the combined data to a new CSV file
df.to_csv('Final_Indian_Recipe_Dateset.csv', index=False)
