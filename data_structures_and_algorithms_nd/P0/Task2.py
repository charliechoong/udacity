"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
durations = {}
for call in calls:
    caller, receiver, duration = call[0], call[1], int(call[3])
    if caller in durations:
        durations[caller] += duration
    else:
        durations[caller] = duration
    if receiver in durations:
        durations[receiver] += duration
    else:
        durations[receiver] = duration

telephone_number, total_time = None, None
for number, duration in durations.items():
    if total_time is None or duration > total_time:
        telephone_number, total_time = number, duration
print(f"{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")
