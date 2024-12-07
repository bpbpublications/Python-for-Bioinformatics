import re
sequence = "ATGAGGGCTAGGCTGATCGATCGATCGTAGCTAGCTAGCTAGCTAG"
pattern = r"(ATG)(.*?)(TAG)"
# The findall function will search for pattern $TAG at the end of the sequence
# The function will return the list of patterns found
matches = re.search(pattern, sequence)
print(matches) 
if matches:
    full_match=matches.group(0) #The entire matched pattern
    start_codon=matches.group(1) # Contents of the first capturing group
    middle_part=matches.group(2) # Contents of the second capturing group
    stop_codon=matches.group(3)  # Contents of the third capturing group
    print("Full Match:", full_match)
    print("Start Codon:", start_codon)
    print("Middle Part:", middle_part)
    print("Stop Codon:", stop_codon)
