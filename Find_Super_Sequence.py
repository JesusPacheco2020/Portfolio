# BTEC 4300: Principles of Bioinformatics
# Graduate HW6

# Super sequence (superstring):
# a larger sequence containing every one of the smaller strings as a substring
# a sequence that can be derived from combining the DNA fragments

# Input: DNA sequences
# >Rosalind_56
# ATTAGACCTG
# >Rosalind_57
# CCTGCCGGAA
# >Rosalind_58
# AGACCTGCCG
# >Rosalind_59
# GCCGGAATAC

# Output: Single longest DNA super sequence
# ATTAGACCTGCCGGAATAC

# ATTAGACCTG
#    AGACCTGCCG
#       CCTGCCGGAA
#          GCCGGAATAC



from Bio import SeqIO

# get the shortest super sequence
def shortestSuperSeq(records):
    graph = create_graph(records)
    start = find_start(graph)
    assembly = assemble(graph,start)
    return assembly

# Build possible graphs
def create_graph(records):
    graph = {}
    for rec1 in records:
        for rec2 in records:
            if rec1.id != rec2.id:
                edge = overlap(str(rec1.seq),str(rec2.seq))
                if edge:
                    graph[str(rec1.seq)] = edge
    return graph

# An overlap will show you where to add an edge to the graph
def overlap(seq1, seq2):
    half = int(len(seq1)/2)
    
    position = seq1.find(seq2[:half])
    if position <0:
        return None
    
    while position >0:
        half += 1
        position = seq1.find(seq2[:half])
    return seq2, half-1

# Get the key of the starting sequence
def find_start(graph):
    for key in graph.keys():
        if key not in [edge[0] for edge in graph.values()]:
            return key
        
   
def assemble(graph, key, result=None):
    if not result:
        result = key
    if not graph.get(key):
        return result
    else:
        edge = graph.get(key)
        merge = result[:-edge[1]] +edge[0]
    return assemble(graph,edge[0],merge)

records = [record for record in SeqIO.parse('rosalind_grad.txt','fasta')]
print(shortestSuperSeq(records))    
