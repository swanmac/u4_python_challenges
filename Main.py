# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# ====================
# def convert_to_preferred_format(sec):
#    sec = sec % (24 * 3600)
#    hour = sec // 3600
#    sec %= 3600
#    min = sec // 60
#    sec %= 60
#    print("seconds value in hours:",hour)
#    print("seconds value in minutes:",min)
#    return "%02d:%02d:%02d" % (hour, min, sec) 

# n = 10000
# print("Time in preferred format :-",convert_to_preferred_format(n))
# ==================
# def convert_min_to_sec(sec):
    # sec = sec % (24 * 3600)
    # hour = sec // 3600
    # sec %= 3600
#     min = sec // 60
#     sec %= 60
#     print("minutes value in seconds:",sec)
#     print("seconds value in minutes:",min)
#     return (min, sec)
# n = 60   
# print("minute to seconds :-",convert_min_to_sec(n)) 
# ==================
from datetime import timedelta

def get_time_hh_mm_ss(sec):
    # create timedelta and convert it into string
    td_str = str(timedelta(seconds=sec))
    print('Time in seconds:', sec)

    # split string into individual component
    x = td_str.split(':')
    print('Time in hh:mm:ss:', x[0], 'Hours', x[1], 'Minutes', x[2], 'Seconds')

# get_time_hh_mm_ss(29500)
# get_time_hh_mm_ss(7500040)
# get_time_hh_mm_ss(60)
# get_time_hh_mm_ss(3600)
# get_time_hh_mm_ss(86400)
# get_time_hh_mm_ss(2592000)



# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->
# Time in seconds: 60   
# Time in hh:mm:ss: 0 Hours 01 Minutes 00 Seconds
# Time in seconds: 3600
# Time in hh:mm:ss: 1 Hours 00 Minutes 00 Seconds
# Time in seconds: 86400
# Time in hh:mm:ss: 1 day, 0 Hours 00 Minutes 00 Seconds
# Time in seconds: 2592000
# Time in hh:mm:ss: 30 days, 0 Hours 00 Minutes 00 Seconds  (June)
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
def middle(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
print(middle("abc"))
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
def maskify(cc):
    str = ''
    for char in cc[:-4]:
        str += '#'
    str += cc[-4:]
    return str
print(maskify("4259 9826 4026 9299"))    
# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->
def online_count(my_dict):
    count=0
    for i in my_dict.values():
        if i == "online":
            count+=1
    return count 

my_dict = {"John":"online",
            "Paul":"online",
            "Ringo":"offline",}
ans = online_count(my_dict)            
print(ans)
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
def discount(price, off):
    percent= off/100
    #print(percent)
    amt_discount = percent * price
    # print(amt_discount)
    savings = price - amt_discount
    print(savings)

    # discount(100, 20)
    # discount(80, 20)
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
def pythagoras(leg1, leg2):
    side1 = leg1 ** 2
    side2 = leg2 ** 2
    hypotenouse = side1 + side2
    print(hypotenouse)
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
def fib(num1, num2):
    count = 9
    fib = [num1, num2]
    for each in range(0,count+1):
        fib.append(fib[-1]+fib[-2])
        return fib
        # ---------------------------------
