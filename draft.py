#!/usr/local/bin/python3
#get the file(test)
tor = open("testor.fasta").read().split('\n')
tda = open("testda.fasta").read().split('\n')
tba = open("testba.fasta").read().split('\n')
tba2 = open("testba2.fasta").read().split('\n')
tls = [tor,tda,tba,tba2]
#



def fasta(path="/localdisk/home/s2232496/AY21A2/"):
	with open("/localdisk/home/s2232496/AY21A2/",'r') as f:
		f = f.read()
