'''
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

def calculate_gc_content(sequences: list[tuple[str, str]]):
    curr_max = ('', 0)
    for each_sequence in sequences:
        # Calculate the percentage, somewhat inefficient considering we're doing multiple counts.
        # Another strategy would be to do one iteration over the whole thing, but O(2n) is just O(n) anyway.
        gc_percentage = ((each_sequence[1].count('G') + each_sequence[1].count('C')) / len(each_sequence[1]))
        # Using a lambda for the max since I'm holding the answer as a tuple of (NAME, percentage) so we want the max of the second value or [1]
        curr_max = max(curr_max, (each_sequence[0], gc_percentage), key=lambda item: item[1])
    # Problem requires we return percentage, not just decimal so multiply by 100
    return (curr_max[0], curr_max[1] * 100)


if __name__ == "__main__":
    sequences = []
    with open("gc/rosalind_gc.txt", 'r') as file:
        # Going to custom read the FASTA format rather than any imports
        while True:
            # Read the first line which should have the name of it
            format = file.readline()
            if not format: break
            # Replace endline and fasta format
            name = format.replace('>', '').replace('\n', '')

            sequence = ''
            # For some reason, each line is broken up by new characters so we have to read each line until we either find a name or it's end of file.
            while True:
                each_subseq_line = file.tell()
                each_subseq = file.readline()
                # If introduction line, or end of file, go back to prior line to redo the above loop.
                if ">" in each_subseq or not each_subseq:
                    file.seek(each_subseq_line)
                    break
                sequence = sequence + each_subseq.replace('\n', '')

            sequences.append((name, sequence))

    print('\n'.join(str(num) for num in calculate_gc_content(sequences)))

