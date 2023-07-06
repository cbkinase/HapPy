import networkx as nx


def create_graph(matrix):
    """
    Input matrix is a binary matrix where each row represents a read and each column represents a variant.
    The value at position (i, j) is 1 if read i has allele 1 at variant j, and 0 otherwise
    """
    G = nx.DiGraph()

    G.add_node('source')
    G.add_node('sink')

    n_reads, n_variants = len(matrix), len(matrix[0])

    for i in range(n_variants):
        # For each variant, we create two nodes: one for allele 0 and one for allele 1
        G.add_node((i, 0))
        G.add_node((i, 1))

        # For source to variant, capacity is the number of reads with 0 in that variant position
        # For variant to sink, capacity is the number of reads with 1 in that variant position
        G.add_edge('source', (i, 0), capacity=[row[i] for row in matrix].count(0), weight=0)
        G.add_edge((i, 1), 'sink', capacity=[row[i] for row in matrix].count(1), weight=0)
    # Edges for reads
    for i, read in enumerate(matrix):
        for j, allele in enumerate(read):
            G.add_edge((j, allele), (j, 1 - allele), capacity=1, weight=1)

    return G


def haplotype_assembly(graph, source, sink):
    cut_value, partition = nx.minimum_cut(graph, source, sink, capacity='capacity')

    # The partition is a tuple of two sets of nodes
    # Each set represents one of the two haplotypes
    # But we have to remove the source and sink
    # Since we are only interested in the variant nodes
    haplotype_1 = {node for node in partition[0] if node != 'source' and node != 'sink'}
    haplotype_2 = {node for node in partition[1] if node != 'source' and node != 'sink'}

    return haplotype_1, haplotype_2, cut_value
