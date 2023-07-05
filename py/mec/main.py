import numpy as np


def mec_greedy(matrix):
    n, m = matrix.shape  # Number of fragments and positions

    # Initialize haplotypes with the majority allele at each position
    haplotype_1 = np.array([np.bincount(matrix[:, j]).argmax() for j in range(m)])
    haplotype_2 = 1 - haplotype_1  # The other allele

    # Correct the haplotypes greedily
    for _ in range(n):
        min_errors = n
        for j in range(m):
            # Try flipping the allele at position j in haplotype_1
            temp = haplotype_1.copy()
            temp[j] = 1 - temp[j]

            # Calculate the total number of mismatches with the fragments
            # TODO: optimize here
            errors = sum(sum(temp != matrix[i]) for i in range(n))

            if errors < min_errors:
                best_haplotype = temp
                min_errors = errors

        haplotype_1 = best_haplotype

    return haplotype_1, haplotype_2
