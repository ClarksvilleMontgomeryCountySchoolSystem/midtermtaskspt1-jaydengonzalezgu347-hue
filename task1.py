# TEST DATA - Do not modify
creator_name = "DigitalDreamer"
current_followers = 4567
starting_followers = 2100
days_tracked = 45
milestone_increment = 1000

# YOUR CODE BELOW THIS LINE
# Calculate follower statistics and milestone progress

# Calculate milestone progress
current_milestone = 4
progress_in_milestone = current_followers // milestone_increment

# Calculate growth statistics
total_growth = current_followers - starting_followers
daily_average = total_growth // days_tracked
# Calculate projections
days_to_milestone = milestone_increment % progress_in_milestone
weekly_growth = daily_average * 7
# Display results with f-strings
print("Creator: {creator_name}")
print("Current Milestone: {current_milestone}")
print("Progress in Milestone {progress_in_milestone}")
print("Total Growth: {total_growth}")
print("Daily Average: {daily_average}")
print("Days to next Milestone: {days_to_milestone}")
print("Weekly Growth Projection: {weekly_growth}")
