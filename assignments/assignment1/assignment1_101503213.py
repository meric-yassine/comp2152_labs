"""
Author: Meric Yassine
Assignment: #1
"""

gym_member = "Alex Alliton"  # Data Type: string
preferred_weight = 20.5      # Data Type: float
highest_reps = 25            # Data Type: integer
membership_active = True     # Data Type: boolean

# A dictionary with 3 strings as Keys, and tuples containing 3 integers as Values.
workout_stats =  {"Alex": (65, 45, 20),
                  "Jamie": (40, 90, 10),
                  "Taylor": (15, 40, 55)}

for friend, stat in list(workout_stats.items()):
    total_minutes = sum(stat)
    workout_stats[f"{friend}_Total"] = total_minutes

# A nested list containing the tuple values of the dictionary (workout_stats) for each friend
workout_list = [list(stat) for stat in workout_stats.values() if isinstance(stat, tuple)]

# Extracting and printing the minutes for yoga and running for each friend. (first two columns of workout_list)
yoga_running_list = [minutes[:2] for minutes in workout_list]
print(yoga_running_list)

# Extracting and printing the minutes for weightlifting for the last two friends. (the last column of the last two rows of workout_list)
weightlifting_last_two = [minutes[2] for minutes in workout_list[1:]]
print(weightlifting_last_two)

# Determining the active friends
for friend, total in workout_stats.items():
    if friend.endswith("Total") and total > 120:
        active_friends = friend.replace("_Total", "")
        print(f"Great job staying active {active_friends}!")

# Searching for a name in the record.
name = input("Who are you looking for?")
if name in workout_stats:
    for friend, stat in workout_stats.items():
        if friend.startswith(name):
            print(friend, stat)
else:
    print(f"Friend {name} not found in the records.")

# Initializing a list with friends names and their total workout minutes.
total_workout = []
for friend, total in workout_stats.items():
    if friend.endswith("Total"):
        friend = friend.replace("_Total", "")
        total_workout.append((friend, total))

# Finding the friend with the highest workout minutes.
highest_friend = ""
highest_minutes = 0

for friend, minutes in total_workout:
    if minutes > highest_minutes:
        highest_friend = friend
        highest_minutes = minutes

# Finding the friend with the lowest workout minutes.
lowest_friend = ""
lowest_minutes = float('inf')

for friend, minutes in total_workout:
    if minutes < lowest_minutes:
        lowest_friend = friend
        lowest_minutes = minutes

# Printing the friends with the highest and the lowest workout results.
print(f"The friend with the highest total workout minutes: {highest_friend}")
print(f"The friend with the lowest total workout minutes: {lowest_friend}")









