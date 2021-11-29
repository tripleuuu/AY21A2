#!/usr/local/bin/python3
#test protein family set: glucose-6-phosphatase in birds (Aves)
#This step it to get the file from NCBI using edirect

#to run commands in bash
import os, subprocess 

#make the pullseq available
puls="PATH=$PATH:/localdisk/data/BPSM/Assignment2/"
subprocess.call(puls,shell=True)

#obtain the protein family files and its namelist 
#def importf(family="glucose-6-phosphatase in birds (Aves)"):
#def importf(family="glucose-6-phosphatase in Aves"):
#ATTENTION: thinking ...
family=input("What's the name of the protein family?\n")
getfile="esearch -db protein -query '{}' | efetch -format fasta > '{}.fasta'".format(family,family)
subprocess.call(getfile,shell=True)
#checkpoint of file existing
try:
    with open('{}.fasta'.format(family)) as f:
        print(f.readline())
        print('There it is!')
except IOError:
    print("File not accessible, please try to use 'AND, OR,etc' to link the keywords.)")

#ATTENTION: Not sure whether required
#get the seqs with glucose-6-phosphatase in header 
getseq="pullseq -i "glucose-6-phosphatase in Aves.fasta" -g glucose-6-phosphatase > glucose-6-phosphatase.fasta"
subprocess.call(getseq,shell=True)

#make files the variable or something in python3
seqlist = open("{}.fasta".format(family)).read().split('>')
#get the individual sequence
os.mkdir("alignoutput")	
	getseq="needle -asequence seqlist -bsequence seqlist -auto -aformat3 pair -outfile ./alignoutput/seq.needle".format(family)
	subprocess.call(getseq,shell=True)

