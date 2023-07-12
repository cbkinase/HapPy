from collections import defaultdict


def overlap(a, b, min_length=3):
    """ Return length of longest suffix of fragment 'a' that overlaps with a prefix of 'b' that is at least 'min_length' characters long.  If no such overlap exists, return 0. """
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1


def create_overlap_graph(reads, min_length):
    """ Create a graph where nodes are reads and edges represent overlap between reads """
    overlaps = defaultdict(list)
    for i, read_a in enumerate(reads):
        for j, read_b in enumerate(reads):
            if i != j:
                overlap_len = overlap(read_a, read_b, min_length)
                if overlap_len > 0:
                    overlaps[read_a].append((read_b, overlap_len))
    return overlaps
