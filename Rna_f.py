def obtainNucleotidesList(numConjoin):

	nucleotides = []
	for i in itertools.product('AGUC', repeat=numConjoin):
		nucleotides.append(''.join(i))

	return nucleotides

def generateCsvFormatNoteLine(nucleotides):
	noteLine = f"{nucleotides[0]}_f"
	for eachNuc in nucleotides[1:]:
		noteLine += ",%s_f"%(eachNuc)

	return noteLine+'\n'
	
def calculateOccurenceFrequency(sequence, numConjoin, nucleotides):
	featureValueStr=''
	seqLen = len(sequence)
	kTuples = []  # All numConjoin in a sequence
	for i in range(seqLen-numConjoin+1):
		kTuples.append(sequence[i:i+numConjoin])
		
	occurfrequency = dict()
	tupleLen = len(kTuples)
	for each in nucleotides:
		occurfrequency[each] = kTuples.count(each)/tupleLen
		featureValueStr += ',%.16f'%(occurfrequency[each])
	return featureValueStr[1:]+'\n'

def generateCsvFormatFrequencyLine(in_file, out_file, numConjoin,nucleotides):
	g = open(out_file,'w')
	g.write(generateCsvFormatNoteLine(nucleotides))
	g.close()

	f = open(in_file)
	count_line = 0
	for eachline in f:
		if eachline[0] == '>':
			continue
			# count_line += 1
#print("  Calculating: sequence-%d"%count_line)
			# sampleType = re.findall(r'\|(\d)', eachline)[0]
		else:
			sequence = eachline.strip()
			tempLine = calculateOccurenceFrequency(sequence, numConjoin, nucleotides)
			g = open(out_file,'a')
			# print("***************************************",tempLine)
			g.write("%s"%(tempLine))
			g.close()

	f.close()

import re
import sys
import itertools
import os


in_file = sys.argv[1]
#numConjoin=1
#out_file = r'./mi%sConjoin_freq.csv'%(numConjoin)
for numConjoin in range(2,6):
	out_file = f'./feature_cache/{in_file[-7]}_%s.csv'%(numConjoin)
	nucleotides = obtainNucleotidesList(numConjoin)
	generateCsvFormatFrequencyLine(in_file, out_file, numConjoin,nucleotides)
	# print("------n=%s Finished!------"%(numConjoin))

# if __name__ == '__main__':
	# nucleotides = obtainNucleotidesList(numConjoin)
	# generateCsvFormatFrequencyLine(in_file, out_file, numConjoin,nucleotides)
	# print("------n=%s Finished!------"%(numConjoin))

#Rna_f.py	
