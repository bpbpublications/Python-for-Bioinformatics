import re
sequence = "ATCGATCGAAGTACG"
pattern = "AAG"
# The pattern will be searced in the sequence and will return the first occurence of the pattern match
matches = re.search(pattern, sequence)
print(matches)
if matches:
    print("Pattern found in the sequence.")
else:
    print("Pattern not found in the sequence.")
