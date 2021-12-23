import json

with open('bogie.json') as f:
  data = json.load(f)

with open('bogie2.json', 'w') as g:
  json.dump(data, g, indent=2,sort_keys=True)