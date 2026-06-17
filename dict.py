student = {
    "student1": {
    "name": "John Doe",
        "age": 20,
        "major": "Computer Science"
    },
    "student2": {
    "name": "Jane Smith",
    "age": 22,
    "major": "Mathematics"

},

"student3": {
    "name": "Alice Johnson",    
    "age": 21,
    "major": "Physics"
},
}
print(student["student2"]["name"])
for student_id, details in student.items():
    print(student_id)
    for key, value in details.items():
        print(f"{key}: {value}")    