from urllib import request
import json

url = "https://api.jokes.one/jod?category=knock-knock"

r= request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)


class Joke:

  def __init__(self, category, description) -> None:
    self.description = description
    self.category = category

  def __str__(self) -> str:
    return f"setup {self.category} description {self.description}"
    
jokes = []


for j in jsonData:
  category = j["category"]
  description = j["description"]
  joke = Joke(description)
  jokes.append(joke)


print(f" Got {len(jokes)} jokes")

for joke in jokes:
  print(joke)
