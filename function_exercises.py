#1 Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n == 2 or n == '2':
        return True
    return False

is_two('3')

#2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise
def is_vowel(char):
    if char in 'aeiou' and len(char) == 1:
        return True
    return False
is_vowel('a')

#3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(char):
    if char not in 'aeiou' and len(char) == 1:
        return True
    return False

is_consonant('g')

#4 Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capit_word(string):
    if string[0] not in 'aeiou':
        string = string[0].upper() + string[1:]
    return string
capit_word('bla')

#5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(bill, percentage):
    if percentage > 0 and percentage < 1:
        return bill * (1 + percentage)
    elif percentage > 0 and percentage < 100:
        return bill * (1 + percentage / 100)
    return bill

calculate_tip(35, 20)

#6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount):
    if discount > 0 and discount < 1:
        return price * (1 - discount)
    elif discount > 0 and discount < 100:
        return price * (1 - discount / 100)
    return price

apply_discount(100, 0.2)

#7 Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(str_with_commas):
    string = ''
    for s in str_with_commas:
        if s != ',':
            string = string + s
            #print(string)
    return int(string)

handle_commas('100,000')

#8 Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    if grade < 60:
        return 'F'
    elif grade >= 60 and grade < 67:
        return 'D'
    elif grade >= 67 and grade < 80:
        return 'C'
    elif grade >= 80 and grade <= 87:
        return 'B'
    return 'A'

get_letter_grade(89)

#9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    st = ''
    for s in string:
        if s not in 'aeiou':
            st += s
    return st

remove_vowels('Mirzakhani')

#10 Define a function named normalize_name. It should accept a string and return a valid python identifier
def normalize_name(name):
    
    name = name.lower()
    name = name.strip()
    
    accepted_letters = list(map(chr, range(97, 123))) #ascii values
    numbers = list(range(10))
    accepted_values = accepted_letters + numbers
    
    for letter in name:
        if letter not in accepted_values:
            name = name.replace(letter, '')
        elif letter == ' ':
            name = name.replace(letter, '_')
    return name
normalize_name('  %kuku  ')

#11 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(list_numbers):
    list_sums = []
    sum_of_numbers = 0
    
    for i in list_numbers:
        sum_of_numbers += i
        list_sums.append(sum_of_numbers)
    
    return list_sums

cumulative_sum ([1, 2, 3, 4])