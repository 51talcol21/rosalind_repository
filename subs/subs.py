'''
Given: Two DNA strings s and t

Return: All locations of t as a substring of s.
'''

def calculate_motifs(t: str, s_substring: str):
    index_array = []
    # Iterate over our string t
    for (index, _value) in enumerate(t):
        # For each index (char) of t, check if the sub array created from that index to the length of the s_substring is equal to the substring itself.
        if (s_substring == t[index: index + len(s_substring)]):
            # Add that index
            index_array.append(index + 1)
    return index_array

if __name__=="__main__": 
    with open("subs/rosalind_subs.txt", 'r') as file:
        t = file.readline()
        s = file.readline()
    print(' '.join(str(index) for index in calculate_motifs(t, s)))