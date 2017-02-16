import sys
#import re
import MySQLdb


if len(sys.argv)< 6:
    print "USAGE: python%s requires target/tissue/username/password." % (sys.argv[0])
    sys.exit()


miRNA= sys.argv[1]
tissue= sys.argv[2]
outname= sys.argv[3]
username= sys.argv[4]
password= sys.argv[5]

OFH= open(outname, "w")

print >> OFH, "miRNA\tGene\tUnigene-id\tType\tTissue\tGeneChromo\tChromoStart\tChromoEnd\tDescription" 
print "Program is working, please wait."
dbname = 'MAPI_ts'
db = MySQLdb.connect('localhost',username,password,dbname)
cursor = db.cursor()

sql = "select p.miRNA, p.gene, u.unigene, e.type, e.tissue, g.chromosome, g. ch_start, g.ch_end, g.Description from tbl_expression e, tbl_predicted_targets p, tbl_genes g, tbl_unigene_refseq u where g.refseq = p.gene and g.refseq=u.refseq  and  p.gene=u.refseq and u.unigene = e.gene and e.tissue in ('"+tissue+"') and p.miRNA in ('"+miRNA+"') group by  p.gene having count(distinct(p.tool)) >1" 

#sql= Select p.gene from tbl_predicted_targets p,  where p.miRNA =\'"+miRNA+"\' and distinct(count(p.tool)) >=3"

cursor.execute(sql)

for line in cursor.fetchall():
    #line.split()
    miRNA = str(line[0])
    gene= str(line[1])
    unig= str(line[2])
    type1=str(line[3])
    tissue= str(line[4])
    chromosome=str(line[5])
    start= str(line[6])
    end= str(line[7])
    desc= str(line[8])
#    print >> OFH,miRNA\tgene\tunig\ttype1\ttissue\tchromosome\tstart\tend\tdesc
    print>> OFH,"%s   %s    %s    %s    %s    %s    %s    %s   %s" %(miRNA, gene, unig, type1,tissue,chromosome, start, end, desc)


