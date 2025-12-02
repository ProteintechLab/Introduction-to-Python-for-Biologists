# Have a look at the error code at https://learn.ptglab.com/view/courses/python/3293178-coding-examples/10727316-debugging-error-codes

sequence = "ATG cgt TAA" 
def transcribe_dna_to_rna(dna):
    rna = dna.replace('t','U')   
    dna = dna.strip().replace(" ", "")  
    return rna.upper()              
print("RNA:", transcribe_dna_to_rna(sequence))  
print(sequence[0:3]) 
