# Simply a one-liner in python.
if __name__ == "__main__":
    with open("problem_2_rna/rosalind_rna.txt", "r") as file:
        print(file.read().replace("T", "U"))
