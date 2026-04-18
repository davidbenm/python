# import datetime
from datetime import datetime

goal_and_deadline = input("Enter your goal and a deadline in the format 'goal:dd.mm.yyyy':\n")
goal, deadline = goal_and_deadline.split(":", 1)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

# calculate how many days from now till deadline
time_till_deadline = deadline_date - today_date

print(f"Dear user, time remaining to accomplish your goal: {goal}, is {time_till_deadline.days} days.")



