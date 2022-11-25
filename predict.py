import os
import pandas as pd
import numpy as np
import pickle as pkl
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from sklearn.svm import SVC


def predict_2om(A,U,C,G):
	prob = []
	pos = []

	for f in os.listdir(r"target"):
		base = f[0]
		model = open(f"./model/{base}.pkl","rb")
		out_model = pkl.load(model)

		test_data = pd.read_csv(f"./target/{base}.csv", header=0)
		x_test =  np.array(test_data.iloc[:, 0:])
    	# y_test = np.array(test_data.iloc[:,0])

		if base == "A" or base == "U":
			scaler = StandardScaler()
			scaler.fit(x_test)
			x_test = scaler.transform(x_test)
		probs = out_model.predict_proba(x_test)[:, 1]
		if base == "A":
			poss = A
		elif base == "U":
			poss = U
		elif base == "C":
			poss = C
		elif base == "G":
			poss = G
		
		for p in range(len(probs)):
			if probs[p] > 0.5:
				prob.append(probs[p])
				pos.append(poss[p])

	return pos, prob

	# else:
	# 	model = open(f"./model/{base}.pkl","rb")
	# 	out_model = pkl.load(model)

	# 	test_data = pd.read_csv(f"./target/{base}.csv", header=0)
	# 	x_test =  np.array(test_data.iloc[:, 1:])
 #    	y_test = np.array(test_data.iloc[:,0])

	# 	if base == "A" or base == "U":
	# 		scaler = StandardScaler()
	# 		scaler.fit(x_test)
	# 		x_test = scaler.transform(x_test)
	# 	probs = out_model.predict_proba(x_test)[:, 1]
	# 	if base == "A":
	# 		poss = A
	# 	elif base == "U":
	# 		poss = U
	# 	elif base == "C":
	# 		poss = C
	# 	elif base == "G":
	# 		poss = G
		
	# 	for p in range(len(prob)):
	# 		if probs[p] > 0.5:
	# 			prob.append(probs[p])
	# 			pos.append(poss[p])

