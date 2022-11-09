total_seconds = int(input("Type an amount of seconds to convert: "))
def seconds_conversion(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds - hours*3600) // 60
    seconds_remaining = total_seconds - hours*3600 - minutes*60
    return hours, minutes, seconds_remaining
hours, minutes, seconds = seconds_conversion(total_seconds)
print(f"{total_seconds} seconds equivalent to {hours} hours, {minutes} minutes and {seconds} seconds.")

