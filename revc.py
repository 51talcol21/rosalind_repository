sample = "AAAACCCGGT"

# Longer way of doing it using a switch statement and keeping original string in-place.
def complementConvert(DNAString):
    # Create blank string.
    complement = ""

    # Iterate over DNAString
    for eachNucleotide in DNAString:
        # Switch case, basically take eachNucleotide and compare to each case.
        # If so, add the end character to our resulting string.
        match eachNucleotide:
            case "A": complement += "T"
            case "G": complement += "C"
            case "C": complement += "G"
            case "T": complement += "A"

    # Another way would be to declare key-value pair and just iterate and do a bunch of replacements

    # To keep it in alphabetical order, we use sort the string, then convert the resulting array to a string.
    return "".join(sorted(complement))

print(complementConvert(sample))