# https://rosalind.info/problems/revc/

import time
from statistics import mean


def rev_complement(strand: str) -> str:  # Slowest
    comp_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    comp_strand = [comp_map[strand[index]] for index in range(len(strand) - 1, -1, -1)]
    return ''.join(comp_strand)


def rev_complement2(strand: str) -> str:  # Slower
    comp_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    comp_strand = [comp_map[base] for base in reversed(strand)]
    return ''.join(comp_strand)


def rev_complement3(strand: str) -> str:  # Slow
    comp_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    comp_strand = [comp_map[base] for base in strand[::-1]]
    return ''.join(comp_strand)


def rev_complement4(strand: str) -> str:  # Fastest
    table = str.maketrans('ATCG', 'TAGC')
    return strand.translate(table)[::-1]


with open('rosalind_revc.txt', 'r') as f:
    revc = f.read()
    print(rev_complement4(revc))

    # Uncomment below code to benchmark all approaches
    # time1 = []
    # time2 = []
    # time3 = []
    # time4 = []
    # revc = 'AAAACCCGGT' * 10_000_000
    # for i in range(10):
    #     print(f"Iteration {i}")

    #     start = time.time()
    #     revc1 = rev_complement(revc)
    #     time1.append(time.time() - start)

    #     start = time.time()
    #     revc2 = rev_complement2(revc)
    #     time2.append(time.time() - start)

    #     start = time.time()
    #     revc3 = rev_complement3(revc)
    #     time3.append(time.time() - start)

    #     start = time.time()
    #     revc4 = rev_complement4(revc)
    #     time4.append(time.time() - start)

    #     print(revc1 == revc2 == revc3 == revc4)
    # print(mean(time1), mean(time2), mean(time3), mean(time4))