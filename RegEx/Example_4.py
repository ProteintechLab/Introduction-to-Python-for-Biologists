import re
def find_motif_locations(dna, motif):
    return [match.start() +1 for match in re.finditer(f'(?={motif})', dna)]

dna = "GATATATGCATATACTT"
motif = "ATAT"

positions = find_motif_locations(dna, motif)
print(" ".join(map(str, positions)))
