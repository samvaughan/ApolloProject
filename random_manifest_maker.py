import csv
import numpy as np 
from random import shuffle



infile="ApolloImages_MetaFile.csv"


filenames=[]
reader = csv.reader(open(infile, "rb"))

for row in reader:



    filenames.append(row[1])




import itertools
def all_pairs(lst):
    for p in itertools.permutations(lst):
        i = iter(p)
        yield zip(i,i)


test=all_pairs(filenames)

print len(filenames)
import pdb
pdb.set_trace()


shuffle(filenames)


outfile='RandomManifest.csv'
writer = csv.writer(open(outfile, 'wb'), delimiter=',')

cntr=0
print "writing random pairs to csv file"

x=next(all_pairs(filenames))


for pair in x:
    cntr+=1
    
    writer.writerow((cntr, pair[0], pair[1]))
    

print "done"