#!/usr/local/bin/python3
#test species set: Cosmoscarta

#to run commands in bash
import os, subprocess 

#obtain the protein family files and its namelist 
def importf(beast="Cosmoscarta"):
beast=input("What's the name of the species?\n")
getfile1="esearch -db protein -query '{}' | efetch -format fasta > {}.fasta".format(beast,beast)
getfile2="grep '>' {}.fasta | cut -d ' ' -f -1 > namelist_{}".format(beast,beast)
subprocess.call(getfile1,shell=True)
sunprocess.call(getfile2,shell=True)

#make files the variable or something
testvar = str(open("{}.fasta".format(beast)).read().split('>')).split('\\n')



