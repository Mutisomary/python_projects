# Add a dictionary in a list
student_data = [
    {"name": "Mary", "age": 26},
    {"name": "Mutiso", "age": 56}
]

def add_to(name, age):
    new_student= {}
    new_student["name"] = name
    new_student["age"] = age
    student_data.append(new_student)


add_to("Dennis", 28)
print(student_data)
