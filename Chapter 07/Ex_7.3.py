import re
sequence = "ATCGATCGAAGTACTG"
pattern = r"[AT]G"
# The findall function will search for Character Group formation as "AG" and "TG"
# The function will return the list of patterns found
matches = re.findall(pattern, sequence)
print(matches)
if matches:
    print("Pattern(s) found in the sequence.")
    for match in matches:
        print(match)
else:
    print("No patterns found in the sequence.")
