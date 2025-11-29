sequence = "ATGCGT"

# Indexing 
print("The character at position 0 is "+ sequence[0])

# Negative Indexing
print("The character at position -1 is "+ sequence[-1])

# Slicing 
print("The characters from position 0 to 2 inclusive are "+ sequence[0:3])

# Slicing [start:stop:step]
print("The characters from position 0 to 5 inclusive with a step value of 2 are "+sequence[0:6:2])

print("gattaca".capitalize())

print("Gattaca".swapcase())

print("GATTACA".lower()) 

print("gattaca".upper())

print("GATTACA".count("C"))

print("ATG".replace("T","U"))

print("GAPDH/TP53/TDP43".split("/"))

print("  GATTACA.  ".strip())

print("gattaca".find("a"))

print("--".join("gattaca"))
