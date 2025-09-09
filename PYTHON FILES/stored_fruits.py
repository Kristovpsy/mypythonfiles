cart : list[str]
checkout : list[str]

stored_fruits: list[str] = ['Apple', 'Banana', 'Cherry', 'Date', 'Mango']
print(f"Stored Fruits: {stored_fruits}")
for fruit in stored_fruits:
    index = stored_fruits.index(fruit)
    pos = index + 1
    print()
# Output the stored fruits and check availability of a fruit order



