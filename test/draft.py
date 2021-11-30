#!/usr/local/bin/python3
#test protein family set: glucose-6-phosphatase in birds (Aves)

#to run commands in bash
import os, subprocess 
#make function to do it
def runbash(command):
	import subprocess
        subprocess.call(command,shell=True)
        print("Loading function...")

#obtain the protein family files 
family=input("What's the name of the protein family?\n")
if family == "":
	family="glucose-6-phosphatase AND Aves"
#make the variable of the filename (initial file)
name = "{}.fasta".format(family)

#ATTENTION: thinking ...
getfile="esearch -db protein -query '{}' | efetch -format fasta > '{}.fasta'".format(family,family)
runbash(getfile)
#checkpoint of file existing
try:
    with open('{}.fasta'.format(family)) as f:
        print(f.readline())
        print("There it is! Cheers!")
except IOError:
    print("No...File not accessible, please try to use 'AND, OR, etc' within the keywords.")

#choose the work
aim=input("Which one do you want? Can simply type the number\n1.alignment\n2.conservation\n3.find motif")
if aim == "1" or aim.upper() == "ALIGNMENT":
	seqlist = open(name).read().split('>')
	os.mkdir("alignoutput")
	with open(name) as f:
		lines=f.count('>')
		if lines >=1000 :
                        check = input("This file contains lots of sequence. Running the programme will spend lots of time. y/n/pick")
			#notice that the large number of the protein sequence may required the longer time
			#Warning: cannot work with this com
			if check.lower() == "y":
                                alignment="needleall -asequence seqlist -bsequence seqlist -auto -aformat3 pair -outfile ./alignoutput$
                                runbash(alignment)
			elif check.lower() == "pick":  
				#choose some of the protein sequence
				keyword = input("Give me the keywords you want of the protein sequences."
				puls="PATH=$PATH:/localdisk/data/BPSM/Assignment2/"
				runbash(puls)
				#get the seqs with keywords in header
				getseq="pullseq -i name -g keyword > keyword.fasta"
				runbash(getseq)
			else :
				aim=input("Which one do you want? Can simply type the number\n2.conservation\n3.find motif\n4.all\n5.back")  
		else :
			alignment="needleall -asequence seqlist -bsequence seqlist -auto -aformat3 pair -outfile ./alignoutput/'{}.needleall.format(family)'"
			runbash(alignment)
			f.close()
try:
    with open("./alignoutput/'{}.needleall'.format(family)") as f:
        print(f.readline())
        print("There it is! Cheers!")
except IOError:
    print("Sorry...File not accessible, please try another way.")
elif aim == "2" or aim.upper() == "CONSERVATION" :
	plot="plotcon -sequence name -graph svg -winsize 4"
	runbash(plot)
elif aim == "3" or aim.upper() == "FIND MOTIF" :
	seamotif="patmatmotifs -sequence name"
	runbash(seamotif)
#checkpoint of file existing
try:
    with open('{}.patmatmotifs'.format(family)) as f:
        print(f.readline())
        print('There it is! Done!')
except IOError:
    print("Sorry, can't find the file.\nGo back to the first step might work.")
print("Finish!")

