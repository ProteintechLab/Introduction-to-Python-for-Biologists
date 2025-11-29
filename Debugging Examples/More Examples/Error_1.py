from Bio import SeqIo                 # 1
def calculate_gc(seq):
    """Return GC% for a sequence""" 
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

for rec in SeqIO.parse("example.fasta","fasta"):   # 2
    try:
        pct = calculate_gc(rec.seq)
        print(f"{rec.id}: {pct:.2f}%")
    except ZeroDivisionErro:                       # 3
        print(f"{rec.id} empty sequence")
    except:                                        # 4
        print("Unknown error", e)                  # 5
