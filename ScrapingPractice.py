import requests
page = requests.get("https://raw.githack.com/paskorn/DS270-Git2022/master/simple.html")
print(page)
print(page.content)