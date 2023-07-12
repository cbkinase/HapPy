from collections import defaultdict

def debruijn_graph_from_kmers(kmers):
    """
    Create a De Bruijn graph from k-mers.
    Each node in a De Bruijn graph represents
    a sequence of characters of length k (called a k-mer).
    Each directed edge represents an overlap
    of length k-1 between its two nodes.
    """
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def eulerian_path(graph):
    """ Find an Eulerian path given a De Bruijn graph """
    start_node = [node for node in graph if len(graph[node]) - len([1 for target in graph if node in graph[target]]) == 1]
    start_node = start_node[0] if start_node else list(graph.keys())[0]
    path, stack = [], [start_node]
    while stack:
        node = stack[-1]
        if graph[node]:
            stack.append(graph[node].pop(0))
        else:
            path.append(stack.pop())
    return ''.join(segment[0] for segment in path[::-1])

def assemble_sequence_from_reads(reads, k):
    kmers = [read[i:i+k] for read in reads for i in range(len(read)-k+1)]
    debruijn_graph = debruijn_graph_from_kmers(kmers)
    # I should account for cases where there are multiple valid eulerian paths
    # (i.e. there are repeats in the sequence)
    # Should also account for phred quality scores.
    return eulerian_path(debruijn_graph)
