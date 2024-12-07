import re
sequence = "ATCGATCGAAGTACG"
pattern = r"GTA|ACG|AAG"
# All the three pattern will be searced in the sequence
# Function will return boolean value "True" if any one of them is found
# Function will return boolean value "False" if none of them are found
matches = re.search(pattern, sequence)
print(matches)
if matches:
    print("Pattern found in the sequence.")
else:
    print("Pattern not found in the sequence.")
