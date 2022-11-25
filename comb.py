#特征合并程序
import os
import pandas as pd
import shutil


a = 0
u = 0
c = 0
g = 0
afeatures = None
cfeatures = None
gfeatures = None
ufeatures = None

files = os.listdir(r"./feature_cache")

for f_ in files:

    if f_[0] == "A":
        # a += 1
        # if a == 1:
        adata = pd.read_csv(f"./feature_cache/{f_}", header=0)
        # acol = list(adata.columns)
        ax = adata.iloc[:,0:]
        afeatures = pd.concat([afeatures, ax], axis=1)
    if f_[0] == "U":
        # u += 1
        # if u == 1:
        udata = pd.read_csv(f"./feature_cache/{f_}", header=0)
        # ucol = list(udata.columns)
        ux = udata.iloc[:,0:]
        ufeatures = pd.concat([ufeatures, ux], axis=1)
    if f_[0] == "C":
        # c += 1
        # if c == 1:
        cdata = pd.read_csv(f"./feature_cache/{f_}", header=0)
        # ccol = list(cdata.columns)
        cx = cdata.iloc[:,0:]
        cfeatures = pd.concat([cfeatures, cx], axis=1)
    if f_[0] == "G":
        # g += 1
        # if g == 1:
        gdata = pd.read_csv(f"./feature_cache/{f_}", header=0)
        # gcol = list(gdata.columns)
        gx = gdata.iloc[:,0:]
        gfeatures = pd.concat([gfeatures, gx], axis=1)
# shutil.rmtree("feature_cache") 
      

if afeatures is not None:
    afeatures.to_csv(f"./comb_cache/A.csv", index=False)
if cfeatures is not None:
    cfeatures.to_csv(f"./comb_cache/C.csv", index=False)
if gfeatures is not None:
    gfeatures.to_csv(f"./comb_cache/G.csv", index=False)
if ufeatures is not None:
    ufeatures.to_csv(f"./comb_cache/U.csv", index=False)
    