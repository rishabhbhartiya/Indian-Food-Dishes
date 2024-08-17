import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

page_link = soup.findAll("a", class_ = "crd_img")

# Extract the link (href) and title
Title = []
Recipe_Link = []

for i in page_link:
    link = i.get('href')
    title = i.get('title')
    Title.append(title)
    Recipe_Link.append(link)
    
data = {'RECIPE': Title, 'RECIPE_LINK': Recipe_Link}

df = pd.DataFrame(data)
df.to_csv("Indian_Food_Recipe.csv")
