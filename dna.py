sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def getEachNucleotide(DNAString):
    # Declare a dic with each nucleotide, 
    DNADic = {"A": 0, "C": 0, "G": 0, "T": 0}

    # Iterate over each char in the string
    for eachNucleotide in DNAString:
        # Add one to each initial value
        DNADic[eachNucleotide] += 1

    # For the problem, take the dict and turn it into an array by value in ACGT order (alphabetical, ASCII works)
    return list(DNADic.values())

print(getEachNucleotide(sample))