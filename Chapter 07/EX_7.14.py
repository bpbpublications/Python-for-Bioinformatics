import re

sequence = "ATGAGGGCTAGGCTGATCGATCGATCGTAGCTAGCTAGCTAGCTAG"
pattern = r"GCT"  # Pattern to match

matches = re.finditer(pattern, sequence)
for match in matches:
    start_position = match.start()  # Start position of the match
    end_position = match.end()  # End position of the match

    print("Match found at position:", start_position, "-", end_position)
