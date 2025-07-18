import requests

USERNAME = "codeewithmert"
API_URL = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(API_URL)
repos = response.json()

table = "| Proje | Açıklama |\n|---|---|\n"

for repo in repos:
    name = repo["name"]
    desc = repo["description"] or "Açıklama yok"
    url = repo["html_url"]
    table += f"| [{name}]({url}) | {desc} |\n"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start = content.find("## 🌟 Öne Çıkan Projeler")
if start != -1:
    end = content.find("##", start + 1)
    if end != -1:
        content = content[:start] + f"## 🌟 Öne Çıkan Projeler\n\n{table}\n" + content[end:]
    else:
        content = content[:start] + f"## 🌟 Öne Çıkan Projeler\n\n{table}\n"
else:
    content += f"\n## 🌟 Öne Çıkan Projeler\n\n{table}\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
