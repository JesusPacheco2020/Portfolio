#BTEC4300: Principles of Bioinformatics
#Graduate HW4
#Input: lac Operon DNA sequence
#Output: Longest Polypeptide (Protein) called by lacOperon. Molecular Weight


#Open file and get DNA sequence
file = open('lacOperon.fasta')
header = file.readline()
sequence = file.read()
sequence = sequence.replace('\n','')



def translate (seq):
    codon_table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
    peptide = ''
    for start in range (0,len(seq)-2,3):
        codon = seq[start:start+3]
        #Output the codons that will be translated into amino acids
    #    print(codon)
        peptide += codon_table[codon]
    return peptide


def calcMolecularWeight(peptide):
    mol_we_table = {
    'A':89.0935, 'R':174.2017, 'N':132.1184, 'D':133.1032, 
    'C':121.1590, 'E':147.1299, 'Q':146.1451, 'G':75.0669,
    'H':155.1552, 'I':131.1736, 'L':131.1736, 'K':146.1882,
    'M':149.2124, 'F':165.1900, 'P':115.1310, 'S':105.0930,
    'T':119.1197, 'W':204.2262, 'Y':181.1894, 'V':117.1469
    }
    mol_weight = 0
    for aa in peptide:
        #print(aa, mol_we_table[aa])
        mol_weight += mol_we_table[aa]
    return mol_weight



#Identify start, stop codon
STOP_CODONS = ('TAG','TAA','TGA')

orfs = set()
for reading_frame in range (3):
    frame = sequence[reading_frame:]
    for position in range(0,len(frame)-2,3):
        codon = frame[position:position+3]
        #print(codon)
        if codon == 'ATG':
            #print('START')
            start_of_orf = frame[position:]
            orf = ''
            for num in range(0,len(start_of_orf)-2, 3):
                orf += start_of_orf[num:num+3]
                
                if orf.endswith(STOP_CODONS):
                    #Identify the start and end codons and output the information
                    print("Possible ORF: ", orf, "\n")
                    
                    orfs.add(translate(orf[:len(orf)-1]))
                    break

#Output the newly synthesized polypeptide chain (lONGEST ONE ONLY) 
sort_orfs = sorted(orfs, key=lambda i:len(i), reverse=True)[0]
print("Longest Polypeptide: ", sort_orfs)


#Calculate molecular weight
print("Molecular weight of longest peptide: ", calcMolecularWeight(sort_orfs))


sample = "ATGGCCGTGCAGACTTAA"
#print(translate(sample))
