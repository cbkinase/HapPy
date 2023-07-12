import naive, debruijn

reads = ["ACGGTACG", "GTA", "CGTACGTTT", "ACG", "CGT", "ACGACG"]
graph = naive.create_overlap_graph(reads, min_length=2)

for read, edges in graph.items():
    for edge in edges:
        print(f'{read} --> {edge[0]} : {edge[1]}')


seq = debruijn.assemble_sequence_from_reads(reads, k=3)
seq_expected = "TACGGTACGACCCCGGGTTTT"
print(seq)
assert seq == seq_expected
