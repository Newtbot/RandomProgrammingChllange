import datetime as dt
#part 1 
user_input = input("how old are you?: ")

def age_calculator(user_input):
    years = user_input
    years = int(years)
    
    months = years * 12 #simple 
    days = years * 365
    hours = days * 24
    minutes = hours * 60

    print("months: " + str(months) + " days: " + str(days) + " hours: " + str(hours) + " minutes: " + str(minutes))

age_calculator(user_input)

#part 2
input = input("whats your birthday in YYYY-MM-DD: ")
def birthday(input):
    birthday_input = input
    #split by - 
    birthday_input = birthday_input.split("-")
    #print(birthday_input[0]) #year
    #print(birthday_input[1]) #month
    #print(birthday_input[2]) #day

birthday(input)





