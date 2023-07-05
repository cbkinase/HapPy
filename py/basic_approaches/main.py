from Bio import SeqIO
import numpy as np


#TODO: fn/data structure to convert VCF to matrix format


def letter_phred_quality(record):
    return list(zip(record.seq, record._per_letter_annotations['phred_quality']))


def greedy_haplotype_assembly(matrix):
    n, m = matrix.shape
    haplotype_1 = np.zeros(m, dtype=int)
    haplotype_2 = np.zeros(m, dtype=int)

    # Sort fragments by the number of 1s
    sorted_fragments = sorted(matrix, key=lambda row: -sum(row))

    for fragment in sorted_fragments:
        # Calculate Hamming distances to the two current haplotypes
        dist_1 = sum(haplotype_1 != fragment)
        dist_2 = sum(haplotype_2 != fragment)

        # Assign the fragment to the haplotype it's closest to
        if dist_1 < dist_2:
            haplotype_1 = np.maximum(haplotype_1, fragment)
        else:
            haplotype_2 = np.maximum(haplotype_2, fragment)

    return haplotype_1, haplotype_2


for record in SeqIO.parse("../samples/fasta/sample3.fasta", "fasta"):
    print(record.description)
    print(record.seq)


for record in SeqIO.parse("../samples/fastq/sample1.fastq", "fastq"):
    print(record.description)
    print(record.seq)
    print(record.__dict__)
    print(letter_phred_quality(record))

    seq = record.seq
    print(seq.complement())
