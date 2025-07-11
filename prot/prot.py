
# Unfair to make us type this out!
# Not really any other way besides web scraping then converting to a dictionary which would take way longer (unless you're good I guess).

# The only important thing is we will need a termination character, to know when the "stop" is.
# The documents say the letters B, J, O, U, X, and Z are not used, let's just use "X"
PROT_DICT = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
            "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
            "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "UAA": "X", "CAA": "Q", "AAA": "K", "GAA": "E", "UAG": "X", "CAG": "Q", "AAG": "K", "GAG": "E",
            "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "UGA": "X", "CGA": "R", "AGA": "R", "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

def rna_to_protein(rna: str):
    """
    Converts RNA into protein

    Parameters:
        rna: string of RNA

    """
    # Blank string to start it in
    rna_codon = ''

    # For each i from 0 to the length of our RNA sequence, where i will be an increment of 3
    for i in range(0, len(rna), 3):
        # Take our prior RNA string and add the following.
        # Take a chunk out of the string with multiple of 3. I.E. if current i is 3, we will go from index 3 to 6 to get sequence XXX.
        # Use that to access our dictionary.
        rna_codon += PROT_DICT[rna[i:i+3]]
    # Using out stop character, splice the string by the index (location where it starts).
    return rna_codon[:rna_codon.index("X")]

if __name__ == "__main__":
    with open("prot/rosalind_prot.txt", 'r') as f:
        rna_string = f.readline().strip()
    print(rna_to_protein(rna_string))
