# Dictionary for student and classmate details
student = {
    "name": "Lewis Fonsi",
    "address": "City of Candon, Ilocos Sur",
    "age": 18,
    "favorite_number": 25,
    "allowance": 500.00
}

classmate = {
    "name": "Andrea Andres",
    "address": "City of Vigan, Ilocos Sur",
    "age": 21,
    "favorite_number": 700,
    "allowance": 700.00
}

# Store the length of the names in a List
name_lengths = [len(student["name"]), len(classmate["name"])]

# Callable function containing IF...ELIF...ELSE logic from the original code
def compare_names_and_address():
    if "Ilocos Sur" in student["address"] and "Ilocos Sur" in classmate["address"]:
        print(f"{student['name'].upper()} is from {student['address']}.")
        print(f"{classmate['name'].lower()} is from {classmate['address']}.")
    else:
        print("None of the students live in Ilocos Sur.")

    # Check whose name is longer
    if name_lengths[0] > name_lengths[1]:
        print(f"{student['name']} has a longer name than {classmate['name']} with {name_lengths[0]} letters.")
    else:
        print(f"{classmate['name']} has a longer name than {student['name']} with {name_lengths[1]} letters.")

# Call the function for reruns
compare_names_and_address()

# Split the names and display results
student_name_split = student["name"].split(" ")
classmate_name_split = classmate["name"].split(" ")
print(f"One among {student_name_split[0]} or {classmate_name_split[0]} lives in Ilocos Sur.")

# Calculate and print the sum and difference of ages and favorite numbers
print(f"The added age of {student['name']} and {classmate['name']} is {student['age'] + classmate['age']}.")
print(f"The subtracted value of favorite numbers of {student['name']} and {classmate['name']} is {student['favorite_number'] - classmate['favorite_number']}.")

# Calculate and print the combined weekly allowance
combined_weekly_allowance = student["allowance"] + classmate["allowance"]
print(f"The weekly allowance of {student['name']} and {classmate['name']} is {combined_weekly_allowance:.2f} pesos.")

# List operations
class_list = [student["name"], classmate["name"]]
class_list_ext = [student["address"], classmate["address"]]
class_list.extend(class_list_ext)
print("Class List:")
for item in class_list:
    print(item)

# Numerical list operations
class_numbers = [student["age"], student["favorite_number"], int(student["allowance"]), classmate["age"], classmate["favorite_number"], int(classmate["allowance"])]
class_numbers.sort(reverse=True)  # Reverse the sort orderd
print(class_numbers)

# Function to congratulate the student on Quiz 2
def quizTwo(user_name):
    print(f"Congratulations on Quiz 2, {user_name} - Student of CS3B")

# Ask for user input and call the function
user_name = input("Enter your name: ")
quizTwo(user_name)
