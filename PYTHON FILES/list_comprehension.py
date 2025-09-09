

squares = [x**2 for x in range(6)]

print(squares)

even = [x for x in range(12) if x % 2 == 0]
odd = [x for x in range (12) if x % 2 != 0]
label = ["even" if x % 2 == 0 else 'odd' for x in range(5)]
print(even)
print(label) 
print(odd)

pairs =[(x,y) for x in[1, 2]
 for y in [3,4]]
print(pairs)

# dictonaries
student = {
    "name" : "Amit",
     "age" : 21,
     "phone book" : "080560234579",
     "best food" : "croissant"
    
}
print(student["name"])
print(student["age"])
print(student["phone book"])
print(student["best food"])


print(student.get("name"))


print(student.pop("best food"))
print(student.pop("best food","Not found"))
student["fav book"] = "Animal farm"
print(student)

#keys
print(student.keys())
#items
profile_list = list(student.items())
print(profile_list)
#values
print(student.values())
#to check if it exists in the dict
print("Animal farm" in student)
#keys and values are different

student = {
    "name" : "Amit",
     "age" : 21,
     
    
}
student_items = student.items() 
print(student_items)

for name, age in (student.items()):
    print(f" Name {name} Age {age}" )


# combining two dicts together
 
student_2= {
    "name" : "micheal",
     "age"  : "41"

}
student.update(student_2)
print(student)

