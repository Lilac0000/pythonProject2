
user_input = int(input("Enter seconds: "))


if user_input < 0 or user_input >= 8640000:
    print("")
else:

    days = user_input // 86400
    hours = (user_input % 86400) // 3600
    minutes = ((user_input % 86400) % 3600) // 60
    seconds = ((user_input % 86400) % 3600) % 60


    days_word = "days" if days != 1 else "day"
    hours_word = "hours" if hours != 1 else "hour"
    minutes_word = "minutes" if minutes != 1 else "minute"
    seconds_word = "seconds" if seconds != 1 else "second"


    result = f"{days} {days_word}, {hours:02}:{minutes:02}:{seconds:02}"
    print(result)