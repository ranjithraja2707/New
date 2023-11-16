import json
with open('sample.json', 'r') as file:
    data = json.load(file)
print(data)
import json

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
with open('output.json', 'w') as file:
    json.dump(data, file)
import json
json_string = '{"name": "Alice", "age": 25, "city": "London"}'
data = json.loads(json_string)
print(data)

