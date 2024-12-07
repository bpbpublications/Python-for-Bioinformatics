import re
sequence = "ATCGAGCTGAAGTATGAGCCCGCG"
pattern = r"AGC+"
# The findall function will search for pattern ATG*
# The function will return the list of patterns found
matches = re.findall(pattern, sequence)
print(matches) 
if matches:
    print("Pattern(s) found in the sequence.")
    for match in matches:
        print(match)
else:
    print("No patterns found in the sequence.")
