from minimum_cut import create_graph, haplotype_assembly

matrix = [
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
]

graph = create_graph(matrix)
source, sink = 'source', 'sink'
haplotype_1, haplotype_2, cut_value = haplotype_assembly(graph, source, sink)

print(f"Haplotype 1: {haplotype_1}")
print(f"Haplotype 2: {haplotype_2}")
print(f"Cut Value: {cut_value}")
