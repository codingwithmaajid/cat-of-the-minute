import requests

response = requests.get("https://api.thecatapi.com/v1/images/search")

cat_url = response.json()[0]["url"]

readme = f"""# 🐱 Cat of the Minute

This repository automatically fetches a random cat using GitHub Actions.

Last updated automatically.

![Random Cat]({cat_url})
"""

with open("README.md", "w") as file:
    file.write(readme)

print("README updated!")