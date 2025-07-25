# Given that both strings are the same size
# The strategy will be to iterate over both strings with a single index and compare each character one by one.
# Basically, the index being the numbered character in the string.
# In the above example: the first G in sample1 and the first C in sample2 would be index 1, and then the second letter of both being index 2.

def countPountMutations(s: str, t: str):
    # Declare a variable to hold number of mutations.
    mutationCount = 0
    nucleotideTuple = ("A", "T", "C", "G")

    # For each number (i) in the range of 0-Length of string s
    for i in range(len(s)):
        # If each character (letter) at index i are not the same, increase counter.
        # Basically, if the letter at place one and two aren't the same, increase difference count.
        if ((s[i] != t[i]) and s[i] in nucleotideTuple and t[i] in nucleotideTuple): mutationCount += 1

    return mutationCount

if __name__ == "__main__":
    with open("hamm/rosalind_hamm.txt", "r") as file:
        firstSequence = file.readline()
        secondSequence = file.readline()
        print(countPountMutations(firstSequence, secondSequence))