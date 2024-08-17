import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

url = "https://food.ndtv.com/recipe-keema-samosa-with-yogurt-dip-98694"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the recipe title
recipe_title = soup.find("h1", class_ ="sp-ttl").text.strip()

# Extract the recipe info
data = {}
for item in soup.find_all('li', class_='RcpInf_li'):
    label = item.find('span', class_='RcpInf_crd_tx1').text.strip()
    value = item.find('span', class_='RcpInf_crd_tx2')
    data[label] = value.text.strip() if value else 'N/A'

# Extract the ingredients
ingredients = [ingredient.text.strip() for ingredient in soup.find_all('li', class_='RcpIngd-tp_li')]

# Extract the main title
main_title = soup.find('h2', class_='RcHTM_tl').text.strip()

# Extract the recipe steps
steps_dict = {}
sections = soup.find_all(['div', 'h3'], class_=['RcHTM_li', 'RcHTM_su-tl'])

current_section = ''
for section in sections:
    if section.name in ['h2', 'h3']:
        # This is a sub-title for a section
        current_section = section.text.strip()
        steps_dict[current_section] = []  # Initialize an empty list for the current section
    elif section.name == 'div' and current_section:
        # This is a step in the current section
        step_number = section.find('span', class_='RcHTM_cnt').text.strip()
        step_text = section.find('span', class_='RcHTM_li-tx').text.strip()
        
        # Append the step number and text as a dictionary to the list for the current section
        steps_dict[current_section].append({
            'step_number': step_number,
            'step_text': step_text
        })

# Combine all the extracted data into a single dictionary
recipe_data = {
    'Recipe Title': recipe_title,
    'Recipe Info': data,
    'Ingredients': ingredients,
    'Main Title': main_title,
    'Steps': steps_dict
}
# Convert the dictionary to a JSON object
recipe_json = json.dumps(recipe_data, indent=4)

if "/" in recipe_title:
    txt = recipe_title.replace("/", "or")
    file_name = txt+".json"
else: 
    file_name = recipe_title+".json"
    
# Save the JSON object to a file
with open(file_name, "w") as file:
    file.write(recipe_json)

print(f"JSON data has been saved to {file_name}.")
