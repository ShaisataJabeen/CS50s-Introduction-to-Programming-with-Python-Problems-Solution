def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    decimal_time = hours + (minutes / 60)
    return decimal_time


time = input("What time is it? ")
converted_time = convert(time)

if 7.0 <= converted_time <= 8.0:
    print("breakfast time")
elif 12.0 <= converted_time <= 13.0:
    print("lunch time")
elif 18.0 <= converted_time <= 19.0:
    print("dinner time")