#!/usr/local/bin/python3
#test protein family set: glucose-6-phosphatase in birds (Aves)
#This step it to get the file from NCBI using edirect

#to run commands in bash
import os, subprocess 

#obtain the protein family files and its namelist 
#def importf(family="glucose-6-phosphatase in birds (Aves)"):
#ATTENTION thinking ...
family=input("What's the name of the protein family?\n")
getfile="esearch -db protein -query '{}' | efetch -format fasta > '{}.fasta'".format(family,family)
subprocess.call(getfile1,shell=True)

#make files the variable or something in python3
seqlist = open("{}.fasta".format(family)).read().split('>')
#get the individual sequence
os.mkdir("alignoutput")	
	getseq="needle -asequence seqlist -bsequence seqlist -auto -aformat3 pair -outfile ./alignoutput/seq.needle".format(family)
	subprocess.call(getseq,shell=True)

