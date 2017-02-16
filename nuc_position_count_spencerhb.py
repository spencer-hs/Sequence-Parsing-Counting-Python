import sys
#import re                                                                                                                                                             
if len(sys.argv) < 3:
    print "USAGE: python %s input-fastafile output-file" % (sys.argv[0])
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]
INFH = open(infile)
INFH.readline()
OFH = open(outfile, 'w')

dict1 = {}
dict2 = {}
sequence = []
acount = 'A'
ccount = 'C'
gcount = 'G'
tcount = 'T'
ncount = 'N'
total= 0

print>> OFH,  "Pos#  A   |   C|   G|   T|   N| Total| PercentA| PercentC| PercentG| PercentT| PercentN"
for line in INFH:
    line = line.strip()
    sequence.append(line)
sequencelength= len(sequence)
for z in range(0,sequencelength,4):
    extract = sequence[z]
    extractlength= len(extract)
    for i in range(0,extractlength,1):
        nucleotide = extract[i]
        position=i
        dict2.setdefault(position,{})
        dict2[position][nucleotide] = nucleotide

        dict1.setdefault(position,{})
        dict1[position].setdefault(acount, 0)
        dict1[position].setdefault(gcount, 0)
        dict1[position].setdefault(ccount, 0)
        dict1[position].setdefault(tcount, 0)
        dict1[position].setdefault(ncount,0)                                                                                                                          

        if nucleotide == 'A':
            dict1[position][acount] += 1
        elif nucleotide == 'C':
            dict1[position][ccount] += 1
        elif nucleotide == 'G':
            dict1[position][gcount] += 1
        elif nucleotide == 'T':
            dict1[position][tcount] += 1
        else:
            dict1[position][ncount] += 1


for position in dict2:
    A = dict1[position][acount]
    C = dict1[position][ccount]
    G = dict1[position][gcount]
    T = dict1[position][tcount]
    N = dict1[position][ncount]

    total = int(A + C + G + T + N)
    percentA = (float(A) / total) * 100
    percentC = (float(C) / total) * 100
    percentG = (float(G) / total) * 100
    percentT = (float(T) / total) * 100
    percentN = (float(N) / total) * 100
    print>> OFH,"%d   %d    %d    %d    %d    %d    %d    %.2f%%   %.2f%%   %.2f%%   %.2f%%   %.2f%%" %(position, A, C, G, T, N, total, percentA, percentC, percentG,percentT, percentN)
    
