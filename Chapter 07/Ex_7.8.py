import re
sequence = "ATCGATTCGAAGTATTTCGATTTT"
pattern = r"AT{2,4}"
# The findall function will search for pattern GAT?
# The function will return the list of patterns found
matches = re.findall(pattern, sequence)
print(matches) 
if matches:
    print("Pattern(s) found in the sequence.")
    for match in matches:
        print(match)
else:
    print("No patterns found in the sequence.")
