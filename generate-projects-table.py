import requests

USERNAME = "codeewithmert"
API_URL = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"

headers = {
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(API_URL, headers=headers)
repos = response.json()

table = "| Proje | Açıklama | Star | Fork | Issue Açık mı? |\n|---|---|---|---|---|\n"

for repo in repos:
    repo_name = repo["name"]
    if repo_name.lower() == "codeewithmert":
        continue  # codeewithmert projesini atla

    desc = repo["description"] or "Açıklama yok"
    url = repo["html_url"]
    stars = repo["stargazers_count"]
    forks = repo["forks_count"]
    issues_open = "Evet" if repo["has_issues"] else "Hayır"

    table += f"| [{repo_name}]({url}) | {desc} | {stars} | {forks} | {issues_open} |\n"

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
