import re

sequence = "ATGGCGTAGTC"

if re.fullmatch(r"[ATGC]+", sequence):
    print("Valid DNA sequence")
else:
    print("Invalid characters found")
