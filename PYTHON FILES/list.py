#lists
names :list[str]= ['Alice', 'Bob', 'Charlie', 'David', 'Eve','Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']

first_name = names[0]
last_name = names[-1]
print(f"First Name: {first_name}, Last Name: {last_name}")
# Output the first and last names from the list

length_of_list = len(names)
print(f"Length of the list: {length_of_list}")
# Output the length of the list

names.append('Kevin')
print(f"Updated List: {names}")

# Output the updated list after appending a new name
names.remove('Charlie')
print(f"List after removal: {names}")
name_index = names.index('Eve')
print(f"Index of 'Eve': {name_index}")

names.sort()
print(f"Sorted List: {names}")

names.reverse()
print(f"Reversed List: {names}")    

names_pop = names.pop()
print(f"List after pop: {names}")
print(f"Popped Element: {names_pop}")       

names_copy = names.copy()
print(f"Copied List: {names_copy}")

names.clear()
print(f"List after clear: {names}")

names.extend(['Liam', 'Mia', 'Noah'])
print(f"List after extend: {names}")
# Output the list after extending it with new names

names.insert(0, 'Olivia')
print(f"List after insert: {names}")

# Output the list after inserting a new name at the beginning
names_count = names.count('Olivia')
print(f"Count of 'Olivia': {names_count}")    



failed_class = ["fardi","jacques", "loki","jermain"]
pardoned: list[str] = failed_class.copy()
pardoned.remove("jermain")

print(f"{failed_class =}")
print(f"{pardoned =}")



