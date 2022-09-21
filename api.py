import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers) ##important
print(f"Status Code : {r.status_code}")
response_dict = r.json() #Covert Json to Dict

print(response_dict.keys())