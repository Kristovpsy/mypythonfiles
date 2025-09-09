import json

sample_data = {
    "name": "salami",
    "age": "18",
    "Dob":"17/08/98",
    "weight":"64kg",
    "skils":["python","machine learning","web dev"],
    "active": True
}

with open("data.json","w") as f:
    json.dump(sample_data,f, indent=4)


print("data.json created")

with open("data.json","r") as f:
    data = json.load(f)
    print("original Data:")
    print(data)

data["status"] = "processed"

with open("updated_data.json","w") as f:
    json.dump(data ,f, indent=4)

print(("\nUPDATED VERSION Saved"))