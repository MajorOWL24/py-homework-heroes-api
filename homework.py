import requests

heroes = ["Hulk", "Captain America", "Thanos"]
url = "https://superheroapi.com/api/2619421814940190/"

max_int = 0
max_hero = ''

for hero in heroes:
  r = requests.get(url + "search/" + hero)
  i = int(r.json()["results"][0]["powerstats"]["intelligence"])
  if i > max_int:
    max_hero = hero
    max_int = i

print(max_hero)
