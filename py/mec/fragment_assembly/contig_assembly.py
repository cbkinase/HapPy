from debruijn import debruijn_graph_from_kmers

def assemble_contigs_from_reads(reads, k):
    """ Assemble a sequence from reads using a De Bruijn graph """
    # Generate k-mers with a sliding window of length `k`
    kmers = [read[i:i+k] for read in reads for i in range(len(read)-k+1)]
    debruijn = debruijn_graph_from_kmers(kmers)
    contigs = []
    for node in debruijn:
        # Check if current node has more than one outgoing edge
        # in which case, it's the end of a contig.
        # If the current node has more than one incoming edge,
        # it's the start of a contig
        if len(debruijn[node]) != 1 or len([1 for target in debruijn if node in target]) != 1:
            if debruijn[node]:
                # If the current node has outgoing edges (i.e. it's not isolated)
                # create a contig  from each outgoing edge by appending the last character
                # of the target node (k-mer) to the current node.
                # This extends the length of the k-mer by 1.
                for target in debruijn[node]:
                    contigs.append(node + target[-1])
    return contigs


if __name__ == "__main__":
    reads = ["ACGGTACG", "GTA", "CGTACGTTT", "ACG", "CGT"]
    contigs = assemble_contigs_from_reads(reads, k=3)
    print(contigs)

    reads = ["AAAA", "AAAT", "AATA", "ATAG", "TAGT", "AGTT", "GTTT"]
    contigs = assemble_contigs_from_reads(reads, k=3)
    print(contigs)
