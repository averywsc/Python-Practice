# Ask user for their year of birth, current year, usual bedtime, and wake-up time
year_born = int(input("Hey, what year were you born? "))
current_year = int(input("What year is it right now? "))
bedtime = int(input("What time do you normally fall asleep (24-hour format)? "))
wake = int(input("And what time do you normally wake up (24-hour format)? "))

# Calculate the user's age
age = current_year - year_born

# Calculate how many hours of sleep the user gets
if wake >= bedtime:
    hours_slept = wake - bedtime
else:
    hours_slept = (wake + 24) - bedtime

print(f"You sleep for {hours_slept} hours.")

# Recommended sleep guidelines based on age
if age <= 1:
    print("You need 12-15 hours of sleep per day.")
    recommended_sleep = 14  # Average
elif 2 <= age <= 5:
    print("You need 11-14 hours of sleep per day.")
    recommended_sleep = 12.5  # Average
elif 6 <= age <= 13:
    print("You need 9-11 hours of sleep per day.")
    recommended_sleep = 10  # Average
elif 14 <= age <= 17:
    print("You need 8-10 hours of sleep per day.")
    recommended_sleep = 9  # Average
elif 18 <= age <= 64:
    print("You need 7-9 hours of sleep per day.")
    recommended_sleep = 8  # Average
else:
    print("You need 7-8 hours of sleep per day.")
    recommended_sleep = 7.5  # Average

# Calculate the recommended bedtime
ideal_bedtime = wake - recommended_sleep
if ideal_bedtime < 0:
    ideal_bedtime += 24  

# Provide a suggestion
print(f"Based on your age, you should be getting around {recommended_sleep} hours of sleep.")
print(f"To achieve that, you should aim to go to sleep at {ideal_bedtime:00.0f} o clock.")
print("No data given will be stored")


