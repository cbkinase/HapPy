# The question: would I rather introduce a foreign dependency like BioPython?
# Or handle some of this boilerplate myself? Well...

def parse_fasta(filename):
    """Convert a FASTA file into a dictionary mapping sequence IDs to sequences"""
    with open(filename, 'r') as f:
        sequences = {}
        current_id = None
        current_seq = []
        for line in f:
            line = line.rstrip()
            if line.startswith('>'):
                if current_id is not None:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id is not None:
            sequences[current_id] = ''.join(current_seq)
        return sequences
