import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y, '\n')

with open('json_example.json', 'r') as file:
    # convert to Python Dictionary
    data = json.loads(file.read())

    print(data, '\n')

    user = data["users"]
    print(user, '\n')

    print(user[0], '\n')

    print(user[0]["firstName"], '\n')

