"""_summary_
"""

from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline_date = datetime.strptime(input_list[1], "%d.%m.%Y")
today_date = datetime.today()

time_remaining = deadline_date - today_date

print(f"Time remaining for your goal: {goal} is {time_remaining.days} days")
