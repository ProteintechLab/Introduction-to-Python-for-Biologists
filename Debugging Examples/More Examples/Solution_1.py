Solution
from Bio import SeqIO
def calculate_gc(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100 if len(seq) else 0.0

for rec in SeqIO.parse("example.fasta","fasta"):
    try:
        pct = calculate_gc(str(rec.seq))
        print(f"{rec.id}: {pct:.2f}%")
    except ZeroDivisionError:
        print(f"{rec.id} empty sequence")
    except Exception as e:
        print("Unknown error", e)
