# https://rosalind.info/problems/rna/

with open('rosalind_rna.txt', 'r') as f:
    rna = f.read()
    print(rna.replace('T', 'U'))
