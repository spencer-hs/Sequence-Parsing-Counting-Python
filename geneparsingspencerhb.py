import sys

if len(sys.argv) <3:
    print "Usage: python %s requires input output file" % (sys.argv[0])
    sys.exit()

infile= sys.argv[1]
outfile=sys.argv[2]


INFH=open(infile)
header=INFH.readline()
header= header.strip()

OFH=open(outfile, "w")
dict= {}
dict=INFH.readline()
average= 0
maxfpkm=0
minfpkm=0
averagefpkm = 0
sum= 0
noncount=0
totalcount=0
fpkmlist=[]
fpkm_dict = {}
print "Output File = %s" % (outfile)

print>>OFH, "Chromosome\tTotalG\t TotalNon-0\t MinFPKM\t MaxFPKM\t AvgFPKM"

for line in INFH:
    line= line.strip()
    data= line.split("\t")
    locus= data[6]
    locussplit=locus.split(':')
    chromosome= locussplit[0]
    fpkm=float(data[10])
    if fpkm> 0:
        noncount +=1
        sum += fpkm
        fpkmlist.append(fpkm)
    else:
        totalcount +=1

    for fpkm in fpkmlist:
        if noncount>0:
            averagefpkm= sum/noncount
            maxfpkm= max(fpkmlist)
            minfpkm=min(fpkmlist)
        else:
            average= 0
            maxfpkm=0
            minfpkm=0
    print >> OFH, "%s             \t %d     \t %d       \t %f    \t %f    \t  %f" % (chromosome, totalcount, noncount, minfpkm,maxfpkm,averagefpkm)

INFH.close()

