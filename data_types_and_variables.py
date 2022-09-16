"""
You have rented some movies for your kids: 
The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
and Hercules (1 day, you don't know yet if they're going to like it). 
If price for a movie per day is 3 dollars, how much will you have to pay?
"""

little_mermaid = 3
brother_bear = 5
hercules = 1
price_per_day = 3
total_to_pay = price_per_day *\
    (little_mermaid + brother_bear + hercules)

"""
Suppose you're working as a contractor for 3 companies: 
Google, Amazon and Facebook, they pay you a different rate per hour. 
Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
How much will you receive in payment for this week? You worked 10 hours for Facebook, 
6 hours for Google and 4 hours for Amazon.
"""

ggl_per_hour = 400
hrs_for_ggl = 6

amz_per_hour = 380
hrs_for_amz = 4

fb_per_hour = 350
hrs_for_fb = 10

total_pay = ggl_per_hour * hrs_for_ggl +\
    amz_per_hour * hrs_for_amz + fb_per_hour * hrs_for_fb

"""
A student can be enrolled to a class only if the class is not full 
and the class schedule does not conflict with her current schedule.
"""
class_not_full = True
class_schedule = [0, 1, 1, 0, 1]
student_schedule = [1, 0, 0, 1, 0]

def schedule_compare(list1, list2):
    for i in range(5):
        if abs(class_schedule[i] - student_schedule[i]) == 1:
            return True

can_go_to_class = class_not_full and schedule_compare(class_schedule, student_schedule)

"""
A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
Premium members do not need to buy a specific amount of products.
"""

num_of_items = 3
offer_expired = False
premium_member = False

can_buy = num_of_items > 2 and not offer_expired or premium_member

"""
the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace
"""

username = 'codeup'
password = 'notastrongpassword'

can_be_password = len(password) >= 5 and len(username) <= 20 and password != username

######
#bonus

def has_whitespace(string):
    if string[0] == ' ' or string[len(string) - 1] == ' ':
        return True

can_be_password_bonus = can_be_password and not has_whitespace(username) and not has_whitespace(password)

#or
can_be_username = not (username[0] == ' ' or username[len(username) - 1] == ' ')
can_be_password = not (password[0] == ' ' or password[len(password) - 1] == ' ')