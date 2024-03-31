"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Get list of numbers in texts
non_tele = set()
for text in texts:
    caller, receiver = text[0], text[1]
    non_tele.add(caller)
    non_tele.add(receiver)

outgoing = set()
for call in calls:
    caller, receiver = call[0], call[1]
    outgoing.add(caller)
    non_tele.add(receiver)

telemarketers = outgoing.difference(receiver)
print(f"These numbers could be telemarketers: ")
telemarketers = sorted(telemarketers)
for number in telemarketers:
    print(number)
