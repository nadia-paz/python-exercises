students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

#  EXERCISES

#1 How many students are there? 
len(students) # 14

#2 How many students prefer light coffee? For each type of coffee roast?
count = 0
for i in range (0, len(students)):
    if students[i]['coffee_preference'] == 'light':
        count += 1

#3 How many types of each pet are there?
pets = []
for student in students: #a dictionary with sudent info
    for pet in student['pets']: #list of dicts with pets info
        pets.append(pet['species']) # add type of the pet
        #print(pet['species'])
# leave only unique values, convert list to the set and back to the list
unique_pets = list(set(pets))

### create a dictionary with number of each pet
pet_count = {}
for pet in unique_pets:
    i = 0
    for v in pets:
        # count quantity of each pet 
        if v == pet:
            i += 1
    #add to the dict pet as a key and quantity as a value
    pet_count[pet] = i
# returns {'horse': 4, 'cat': 11, 'dog': 3}

#4 How many grades does each student have? Do they all have the same number of grades?
grades_quantity = set()
for student in students:
    grades_quantity.add(len(student['grades']))
print(grades_quantity) # {4}
print(len(grades_quantity)) # 1 value in the set, means all students have the same number of grades

#5 What is each student's grade average?
grades_average = {}
for student in students:
    grades_average[student['student']] = sum(student['grades']) / len(student['grades'])
print(grades_average)
"""
{'Ada Lovelace': 78.5,
 'Thomas Bayes': 83.5,
 'Marie Curie': 73.25,
 'Grace Hopper': 78.5,
 'Alan Turing': 81.5,
 'Rosalind Franklin': 80.75,
 'Elizabeth Blackwell': 84.5,
 'Rene Descartes': 88.75,
 'Ahmed Zewail': 88.75,
 'Chien-Shiung Wu': 82.5,
 'William Sanford Nye': 81.5,
 'Carl Sagan': 91.0,
 'Jane Goodall': 79.0,
 'Richard Feynman': 89.0}
"""

#6 How many pets does each student have?
pets_quantity = {}
for student in students:
    pets_quantity[student['student']] = len(student['pets'])
print(pets_quantity)
"""
{'Ada Lovelace': 1,
 'Thomas Bayes': 0,
 'Marie Curie': 1,
 'Grace Hopper': 2,
 'Alan Turing': 3,
 'Rosalind Franklin': 0,
 'Elizabeth Blackwell': 1,
 'Rene Descartes': 2,
 'Ahmed Zewail': 2,
 'Chien-Shiung Wu': 1,
 'William Sanford Nye': 2,
 'Carl Sagan': 1,
 'Jane Goodall': 1,
 'Richard Feynman': 1}
"""

#7 How many students are in web development? data science?
courses = {'web development', 'data science'}
students_in_course = {}
for course in courses:
    i = 0
    for student in students:
        if student['course'] == course:
            i += 1
    students_in_course[course] = i
students_in_course
"""
{'web development': 7, 'data science': 7}
"""
#8 What is the average number of pets for students in web development?
num_of_pets_webdev = []
for student in students:
    if student['course'] == 'web development':
        num_of_pets_webdev.append(len(student['pets']))
avg_number_pets_webdev = sum(num_of_pets_webdev) / len(num_of_pets_webdev)
avg_number_pets_webdev
# 1.2857142857142858

#9 What is the average pet age for students in data science?
    pet_age_ds = []
for student in students:
    if student['course'] == 'data science':
        for pet in student['pets']:
            pet_age_ds.append(pet['age'])
pets_age_avg_ds = sum(pet_age_ds) / len(pet_age_ds)
pets_age_avg_ds
# 5.444444444444445

#10 What is most frequent coffee preference for data science students?
coffee_preference_set = set() #unique values of coffee preferences
coffee_preference_dict = {} # dictionary to count each coffee preference occurance

# for all students
for student in students:
    coffee_preference_set.add(student['coffee_preference'])
#add keys and values to the dictionary
for cps in coffee_preference_set:
    i = 0
    for student in students:
        if cps == student['coffee_preference']:
            i += 1
    coffee_preference_dict[cps] = i
coffee_preference_dict
# {'medium': 6, 'dark': 5, 'light': 3}
most_frequent_value = max(coffee_preference_dict.values()) #6
most_frequent_key = max(coffee_preference_dict, key = coffee_preference_dict.get) #medium
least_frequent_value = min(coffee_preference_dict.values()) #3
least_frequent_key = min(coffee_preference_dict, key = coffee_preference_dict.get) # light

###########
# for DS students
coffee_preference_dict.clear() # remove all values from the dict

for cps in coffee_preference_set:
    i = 0
    for student in students:
        if cps == student['coffee_preference'] and student['course'] == 'data science':
            i += 1
    coffee_preference_dict[cps] = i

most_frequent_key_ds = max(coffee_preference_dict, key = coffee_preference_dict.get) #medium
most_frequent_value_ds = max(coffee_preference_dict.values())

#11 What is the least frequent coffee preference for web development students?
# use a set and a dict from the previous exercise
coffee_preference_dict.clear() # remove all values from the dict

for cps in coffee_preference_set:
    i = 0
    for student in students:
        if cps == student['coffee_preference'] and student['course'] == 'web development':
            i += 1
    coffee_preference_dict[cps] = i
# {'medium': 2, 'dark': 2, 'light': 3}
# since medium and dark have the smalles number I create a list for least frequent coffee preferences
least_frequent_values_wd = []
for cpd in coffee_preference_dict:
    if coffee_preference_dict[cpd] == min(coffee_preference_dict.values()):
        least_frequent_values_wd.append(cpd)
least_frequent_values_wd # ['medium', 'dark']

#12 What is the average grade for students with at least 2 pets?
grades_of_pet_lovers = []

for student in students:
    if len(student['pets']) >= 2:
        for i in range(0, len(student['grades'])):
            grades_of_pet_lovers.append(student['grades'][i])
avg_grades_of_pet_lovers = sum(grades_of_pet_lovers) / len(grades_of_pet_lovers)
avg_grades_of_pet_lovers
#83.8

#13 How many students have 3 pets?
students_with_3_pets = 0
for student in students:
    if len(student['pets']) == 3:
        students_with_3_pets += 1
students_with_3_pets
# 1

#14 What is the average grade for students with 0 pets?
grades_of_pet_haters = []

for student in students:
    if len(student['pets']) == 0:
        for i in range(0, len(student['grades'])):
            grades_of_pet_haters.append(student['grades'][i])
avg_grades_of_pet_haters = sum(grades_of_pet_lovers) / len(grades_of_pet_lovers)
print(grades_of_pet_haters)
avg_grades_of_pet_haters # 83.8 as well

#15 What is the average grade for web development students? data science students?
grades_wd = [] #grades of web dev students
grades_ds = [] # grades of DS students

for student in students:
    if student['course'] == 'web development':
        for i in range(0, len(student['grades'])):
            grades_wd.append(student['grades'][i])

for student in students:
    if student['course'] == 'data science':
        for i in range(0, len(student['grades'])):
            grades_ds.append(student['grades'][i])

avg_grades_wd = sum(grades_wd) / len(grades_wd)
avg_grades_ds = sum(grades_ds) / len(grades_ds)
print(avg_grades_wd) #~81.18
print(avg_grades_ds) #~84.68


#16 What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
grades_dark_coffee_drinkers = []

for student in students:
    if student['coffee_preference'] == 'dark':
        for i in range(0, len(student['grades'])):
            grades_dark_coffee_drinkers.append(student['grades'][i])

avg_grade_dark_coffee_drinkers = sum(grades_dark_coffee_drinkers) / len(grades_dark_coffee_drinkers)
avg_grade_dark_coffee_drinkers #81.35

#17 What is the average number of pets for medium coffee drinkers?
num_pets_medium_coffee_drinkers = []

for student in students:
    if student['coffee_preference'] == 'medium':
        num_pets_medium_coffee_drinkers.append(len(student['pets']))
avg_num_pets_medium_coffee_drinkers = \
    sum(num_pets_medium_coffee_drinkers) / len(num_pets_medium_coffee_drinkers)
avg_num_pets_medium_coffee_drinkers # ~1.167
#18 What is the most common type of pet for web development students?
pets_webdev = []

for student in students:
    if student['course'] == 'web development':
        for pet in student['pets']:
            pets_webdev.append(pet['species'])
unique_pets_webdev = set(pets_webdev)
unique_pets
pets_webdev_count = {}

for pet in unique_pets_webdev:
    count = 0
    for p in pets_webdev:
        if pet == p:
            count += 1
    pets_webdev_count[pet] = count

print(pets_webdev)
print(pets_webdev_count)

most_common_pet_webdev = max(pets_webdev_count, key = pets_webdev_count.get)
most_common_pet_webdev #horse

#19 What is the average name length?
name_length_list = []

for student in students:
    name_length_list.append(len(student['student']))
avg_name_length = sum(name_length_list) / len(name_length_list)
print(name_length_list)
avg_name_length # ~13.64

#20 What is the highest pet age for light coffee drinkers?
pets_ages_for_medium_coffee_drinkers = []

for student in students:
    if student['coffee_preference'] == 'light':
        for pet in student['pets']:
            pets_ages_for_medium_coffee_drinkers.append(pet['age'])

print(pets_ages_for_medium_coffee_drinkers)
max(pets_ages_for_medium_coffee_drinkers) # 8