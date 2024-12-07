import re
sequence = "ATGAGGGCTAGGCTGATCGATCGATCGTAGCTAGCTAGCTAGCTAG"
pattern = r"ATG"  # Pattern to match
match = re.search(pattern, sequence)
if match:
    start_position = match.start()  # Start position of the match
    end_position = match.end()  # End position of the match

    print("Start position:", start_position)
    print("End position:", end_position)
