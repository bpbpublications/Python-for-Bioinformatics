import re
sequence = "ATGAGGGCTAGGCTGATCGATCGATCGTAGCTAGCTAGCTAGCTAG"
pattern = r"TAG$"
# The findall function will search for pattern $TAG at the end of the sequence
# The function will return the list of patterns found
matches = re.findall(pattern, sequence)
print(matches) 
if matches:
    print("Pattern found at the end of the sequence.")
else:
    print("No patterns found in the sequence.")
