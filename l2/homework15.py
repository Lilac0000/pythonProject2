user_input = int(input("Введіть секунди: "))

if user_input < 0 or user_input >= 8640000:
    print("")
else:
    days = user_input // 86400
    hours = (user_input % 86400) // 3600
    minutes = ((user_input % 86400) % 3600) // 60
    seconds = ((user_input % 86400) % 3600) % 60

    days_word = "днів" if days != 1 else "день"
    hours_word = "годин" if hours != 1 else "година"
    minutes_word = "хвилин" if minutes != 1 else "хвилина"
    seconds_word = "секунд" if seconds != 1 else "секунда"

    result = f"{days} {days_word}, {hours:02}:{minutes:02}:{seconds:02}"
    print(result)