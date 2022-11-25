import os
import pandas as pd
import shutil


files = os.listdir(r"./comb_cache")

n = {"A":308, "C":313, "G":908, "U":163}
out_data = None


for i in files:
    #print(i)
    order_data = pd.read_csv(f"./feature/{i}", header=0)
    data = pd.read_csv(f"./comb_cache/{i}", header=0)
    order_col = list(order_data.columns[:n[i[0]]])[1:]
    out_data = None
    # print(data["GA_f"])
    for m in order_col:
        out_data = pd.concat([out_data, data[m]], axis=1)
    # print(out_data)
    out_data.to_csv(f"./target/{i[0]}.csv", index=False)

# shutil.rmtree("./feature_cache")