name = "Jose maria Carlington "

print(f"{name =}")

print(f"{name.title() =}")
print(f"{name.istitle()=}")
print(f"{name.upper()=}")
print(f"{name.lower()=}")
print(f"{name.isupper()}")
print(f"{name.islower()}")
print(f"{name.isalpha()}")
print(f"{name.isdigit()}")
print(f"{name.isdigit()}")
print(f"{name.isalnum()}")
print(f"{name.casefold()}")


names :list[str] = [
    "Maxwell",
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy"

]

for name1 in names:
    print(f"i have slapped {name1.title()}  for being a bad person")

range_of_names = range(0, 12, 2)
for i in range_of_names:
    print(f"Name at index {i}: {names[i]}")


num = [22, 36, 
       50, 64, 78, 92, 104, 120, 114, 134,148,162, 176, 190]
range_of_num = range(0, len(num), 2)
for i in range_of_num:
    print(f"Number at index {i}: {num[i]}")




list_of_names :list[str] = ["jeremy","allen", "james", "kuda", "maria", "jose", "carlington"]

print(f"{list_of_names =}")
names_count = list_of_names.count("jeremy")
print(f"the name count of jeremy {names_count =}")

saints_name = "andre palooza"

print(f"{saints_name = }")

print(f"{saints_name.title()}")
print(f"{saints_name.istitle()}")
print(f"{saints_name.isalnum()}")
print(f"{saints_name.split()}")
print(f"{saints_name.strip()}")
print(saints_name)

no_list =[10,7,8,9,0,7,9,7,8,9,12,6]
no_list[0]
print(no_list[5])
range_no = range(0 ,len(no_list),1)
for i in range_no:
    print(f"numbers{i}:{no_list[i]}")