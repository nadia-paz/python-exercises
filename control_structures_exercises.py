"""
Conditional Basics

- prompt the user for a day of the week, print out whether the day is Monday or not
- prompt the user for a day of the week, print out whether the day is a weekday or a weekend
create variables and make up values for
- the number of hours worked in one week
- the hourly rate
- how much the week's paycheck will be
write the python code that calculates the weekly paycheck. 
You get paid time and a half if you work more 
than 40 hours
"""

day_of_week = input('Enter the day of the week ')
if day_of_week.lower() == 'monday' or day_of_week.lower() == 'mon':
    print("It's Monday")
else:
    print("Friday is coming soon!")

day_of_week = input('Enter the day of the week ')
day_of_week = day_of_week.lower()
if day_of_week == 'saturday' or day_of_week == 'sat' or day_of_week == 'sunday' or day_of_week == 'sun':
        print("Weekend")
else:
    print('Weekday')

hrs_worked = 41
hr_rate = 100
pay_check = hrs_worked * hr_rate

if hrs_worked > 40:
    pay_check *= 1.5   
pay_check

"""
WHILE LOOPS
"""

#1
i = 5

while i <= 15:
    print(i)
    i += 1

#2
i = 0

while i <= 100:
    print(i, end = ' ')
    i += 2

#3
i = 100

while i >= -10:
    print(i, end = ' ')
    i -= 5

#4
i = 2

while i <= 1_000_000:
    print(i, end = ' ')
    i *= i

#5
i = 100

while i >= 5:
    print(i)
    i -= 5

"""
For Loops
"""

"""
Write some code that prompts the user for a number, 
then shows a multiplication table up through 10 for 
that number.
"""

number = int(input('enter a number :'))

for n in range(1, 11):
    result = n * number
    print(f'{number} x {n} = {result}')

"""
Create a for loop that uses print to create the output shown below.
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
for n in range (1, 10):
    for i in range (0, n):
        print(n, end = ' ')
    print()

"""
break and continue
"""

#1
"""
Write a program that prompts the user for a positive integer. 
Next write a loop that prints out the numbers 
from the number the user entered down to 1.
"""

number = int(input('Enter a positive number: '))

for n in range(0, number):
    print(number)
    number -= 1
    if number == 0:
        break

#2 breaks when reaches user's input
for i in range(0, 1_000_000):
    print(i, end = ' ')
    if i == number:
        break

#3
"""
Prompt the user for an odd number between 1 and 50. 
Use a loop and a break statement to continue prompting 
the user if they enter invalid input. 
(Hint: use the isdigit method on strings to determine 
this). Use a loop and the continue statement to output 
all the odd numbers between 1 and 50, except for the number the user entered.
"""

wrong_input = True
number = 0
while wrong_input:
    user_input = input('Enter an odd number between: ')
    if user_input.isdigit():
        number = int(user_input)
        if number % 2 == 1 or number <= 0:
            wrong_input = False
        else:
            wrong_input = True

for i in range(1, 50, 2):
    if i == number:
        print(f'Yikes! Skipping number: {i}')
        continue
    print(f'Here is an odd number: {i}')

# FIZZBUZZ
for n in range(1, 101):
    if n % 15 == 0:
        print('FIZZBUZZ')
    elif n % 3 == 0:
        print('FIZZ')
    elif n % 5 == 0:
        print('BUZZ')
    else:
        print(n)

#4
"""
Display a table of powers.

Prompt the user to enter an integer.
Display a table of squares and cubes from 1 
to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
Example:
What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
"""

number = int(input('What number would you like to go up to? '))

print ("{:<8} {:<10} {:<10}".format('number','squared','cubed'))

if number >= 0:
    for i in range(1, number + 1):
        print ("{:<8} {:<10} {:<10}".format(i, i * i, i *i * i))
else:
    for i in range(number, abs(number) + 1):
        print ("{:<8} {:<10} {:<10}".format(i, i * i, i *i * i))

#5
"""
Convert given number grades into letter grades:
Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
"""

enter_grade = True

while enter_grade:
    grade = int(input('Enter the number 0 to 100: '))
    if grade >= 0 and grade < 60:
        print(f'Your grade is F')
    elif grade >= 60 and grade < 67:
        print(f'Your grade is D')
    elif grade >= 67 and grade < 80:
        print(f'Your grade is C')
    elif grade >= 80 and grade <= 87:
        print(f'Your grade is B')
    else:
        print(f'Your grade is A')
    #ask if user wants to continue
    answer = input('Continue? (y/n) ')
    answer = answer.lower()
    if answer == 'y' or answer == 'yes':
        continue
    else:
        enter_grade = False

#6
"""
Create a list of dictionaries where each dictionary 
represents a book that you have read. 
Each dictionary in the list should have the 
keys title, author, and genre. 
Loop through the list and print out information about 
each book.

Prompt the user to enter a genre, 
then loop through your books list and print 
out the titles of all the books in that genre.

"""
books = [{
    'title': 'Master and Margharita',
    'author': 'Bulgakov',
    'genre': 'fantasy',
},
    {
    'title': 'The Lord of the Rings',
    'author': 'Tolkien',
    'genre': 'fantasy',
},
    {
    'title': 'Shantaram',
    'author': 'Roberts',
    'genre': 'adventure'
},
    {
    'title': 'And Then There Were None',
    'author': 'Christie',
    'genre': 'mystery'
},
    {
    'title': 'Alice\'s Adventures in Wonderland',
    'author': 'Carroll',
    'genre': 'fantasy'
}]

genre = input('Genre: ').lower()
books_found = 0 
for book in books:
    if genre == book['genre']:
        print(book['title'])
        books_found += 1
        
if books_found == 0:
    print('Oooops, no books found. Next time try: fantasy, adventure, mystery')