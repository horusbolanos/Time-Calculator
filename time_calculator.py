def add_time(start, duration, day=None):
    # Convert start time to minutes
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    total_minutes = start_hour * 60 + start_minute

    # Convert duration to minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    total_minutes += duration_hour * 60 + duration_minute

    # Calculate the new time and days
    new_hour = total_minutes // 60
    new_minute = total_minutes % 60
    new_period = period
    days_later = total_minutes // 1440  # 1440 minutes in a day

    # Determine the new period (AM or PM)
    if new_hour >= 12:
        new_period = "PM" if period == "AM" else "AM"
        new_hour %= 12

    # Adjust new_hour for 12:00 PM/AM
    if new_hour == 0:
        new_hour = 12

    # Calculate the new day of the week if day parameter is provided
    if day is not None:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = day.lower().capitalize()
        day_index = (days.index(day) + days_later) % 7
        new_day = days[day_index]

    # Construct the result string
    result = f"{new_hour}:{new_minute:02} {new_period}"
    if day is not None:
        result += f", {new_day}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result

print(add_time("3:00 PM", "3:10"))  # 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday"))  # 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"))  # 12:03 PM
print(add_time("10:10 PM", "3:30"))  # 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday"))  # 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))  # 7:42 AM (9 days later)
