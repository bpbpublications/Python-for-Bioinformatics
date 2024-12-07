import re
sequence = "ATGAGGGCTAGGCTGATCGATCGATCGTAGCTAGCTAGCTAGCTAG"
pattern = r"^ATG"
# The findall function will search for pattern ^ATG at the begining of he sequence
# The function will return the list of patterns found
matches = re.findall(pattern, sequence)
print(matches) 
if matches:
    print("Pattern found at the begining of the sequence.")
else:
    print("No patterns found in the sequence.")
