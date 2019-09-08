import json

with open("./parameters.json") as f:
    df = json.load(f)

print(df)
