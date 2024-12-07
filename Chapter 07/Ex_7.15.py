import re

sequence = "ATCGNNNATCGAAGTACG"
pattern = r"N+"

result = re.split(pattern, sequence)

print("Split sequence:")
for substring in result:
    print(substring)
