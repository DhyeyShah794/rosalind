# https://rosalind.info/problems/dna/

with open('rosalind_dna.txt', 'r') as f:
    dna = f.read()
print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
