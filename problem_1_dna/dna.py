file = open("problem_1_dna/rosalind_dna.txt", "r")

def getEachNucleotide(DNAString: str):
    # Declare a dic with each nucleotide, 
    DNADic = {"A": 0, "C": 0, "G": 0, "T": 0}

    # Iterate over each char in the string
    for eachNucleotide in DNAString:
        # Add one to each initial value
        if eachNucleotide in DNADic: DNADic[eachNucleotide] += 1

    # For the problem, take the dict and turn it into an array by value in ACGT order (alphabetical, ASCII works)
    # To break down the syntax of this, we are taking the values of the DNADic (Number of each nucleotide)
    # Converting it to a list of just those values [20, 12, 17, 21]
    # To convert to the final value of 20 12 17 21, we need to take each number, convert it to a string and then join into a final string
    return " ".join(str(eachVal) for eachVal in list(DNADic.values()))

print(getEachNucleotide(file.read()))
file.close()