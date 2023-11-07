# [[name, sequence], [name, sequence] ...] -> user_fasta_list

import os
import shutil
from predict import *
from ANF import ANF
from NCP import NCP
import sys 
import re


def myMain(user_fasta_list, type_, out_file):

	out = []


	for i in range(len(user_fasta_list)):

		if os.path.exists("./fasta_cache"):
			shutil.rmtree("./fasta_cache")
			os.mkdir("./fasta_cache")
		else:
			os.mkdir("./fasta_cache")
		if os.path.exists("./feature_cache"):
			shutil.rmtree("./feature_cache")
			os.mkdir("./feature_cache")
		else:
			os.mkdir("./feature_cache")
		if os.path.exists("./comb_cache"):
			shutil.rmtree("./comb_cache")
			os.mkdir("./comb_cache")  
		else:
			os.mkdir("./comb_cache")
		if os.path.exists("./target"):
			shutil.rmtree("./target")
			os.mkdir("./target")
		else:
			os.mkdir("./target")   

		#文本序列获取
		title_one = user_fasta_list[i][0].strip()
		title_l = len(title_one)

		padding = "N"*20
		sequence = padding + str(user_fasta_list[i][1]).strip() + padding

		apos = []
		upos = []
		cpos = []
		gpos = []

		for l in range(len(sequence)-40):

			frag = sequence[l:l+41]

			if type_ == "A" or type_ =="all":

				if frag[20] == "A":
					apos.append(l)
					title_two = '>' + str(l)
					with open(r"fasta_cache/A.fasta", "a+") as data_file:
						data_file.write(title_two + "\n" + frag + "\n")

			if type_ == "U" or type_ =="all":

				if frag[20] == "U":
					upos.append(l)
					title_two = '>' + str(l)
					with open(r"fasta_cache/U.fasta", "a+") as data_file:
						data_file.write(title_two + "\n" + frag + "\n")

			if type_ == "C" or type_ =="all":
				if frag[20] == "C":
					cpos.append(l)
					title_two = '>' + str(l)
					with open(r"fasta_cache/C.fasta", "a+") as data_file:
						data_file.write(title_two + "\n" + frag + "\n")

			if type_ == "G" or type_ =="all":

				if frag[20] == "G":
					gpos.append(l)
					title_two = '>' + str(l)
					with open(r"fasta_cache/G.fasta", "a+") as data_file:
						data_file.write(title_two + "\n" + frag + "\n")

		#特征提取
		 
		for f in os.listdir("fasta_cache"):
			ANF(f'{f}')
			NCP(f'{f}')
			os.system("python Rna_f.py ./fasta_cache//%s" % f)

		
		#特征合并
		os.system("python comb.py")
		os.system("python sort_f.py")

		pos, prob = predict_2om(apos,upos,cpos,gpos)

		info = [title_one, user_fasta_list[i][1]]
		# print(info)
		each = []
		each.append(info)
		each.append(pos)
		each.append(prob)

		if os.path.exists("./fasta_cache"):
			shutil.rmtree("./fasta_cache")
			# os.mkdir("./fasta_cache")

		if os.path.exists("./feature_cache"):
			shutil.rmtree("./feature_cache")
			# os.mkdir("./feature_cache")

		if os.path.exists("./comb_cache"):
			shutil.rmtree("./comb_cache")
			# os.mkdir("./comb_cache")

		if os.path.exists("./target"):
			shutil.rmtree("./target")
			# os.mkdir("./target")

		out.append(each)
	with open(out_file, "w") as out_f:
		

		for i in out:
			if i[1] == []:
				out_f.write(str(i[0][0]) + "\nNo 2OM site in this sequence.\n")
			else:
				out_f.write(str(i[0][0]) + "\nposition:" + str(i[1]) + "\nprobability:" + str(i[2]) + "\n")

	return out


# test = [[">A-1|1|training","GAAUGGUCGUUGGAGAUCAGAGUGGAAGUUCACCAUCACACUCCACGUGUGUAUGUGAAUUACAAGAUCCACGUGCAUCGUC"],
# 		[">A-2|1|training","GUAGGAUCCACAGCGAUUAAACGAGAAAAGAUAAUAGUUGAGUUCGUGCAGCGUAGUUUAGAAUCGUCACGUAAAGUGUCGG"]]
# out1 = myMain(test, "all")
# print(out1)

def read_fasta_from_str(fasta_str):

    if fasta_str.find('>') == -1:
        flash('The input file seems not in fasta format.')
        redirect(request.url)

    fasta_str = fasta_str.replace("\r", "")
    records = fasta_str.split('>')[1:]
    myFasta = []
    for fasta in records:
        array = fasta.split('\n')
        name, sequence = array[0].split()[0], re.sub('[^AGTCU-]', '-', ''.join(array[1:]).upper())
        sequence = sequence.replace("T", "U")
        myFasta.append([name, sequence])

    return myFasta

def read_fasta_from_file(file):

    if os.path.exists(file) == False:
        flash('Error: "' + file + '" does not exist.')
        redirect(request.url)

    with open(file) as f:
        records = f.read()

    myFasta = read_fasta_from_str(records)

    return myFasta  



if __name__ == "__main__":
	file_path = sys.argv[1]
	myFasta = read_fasta_from_file(file_path)
	out_file = sys.argv[2]
	type_ = sys.argv[3]
	myMain(myFasta, type_, out_file)
	

    # [
    # [each = [head, sqq], pos = [position], prob = [prob]],
    # [[head, sqq], [position], [prob]],
    # ]
