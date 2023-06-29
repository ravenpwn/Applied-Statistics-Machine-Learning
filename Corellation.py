import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

#THIS IS TO FIND COLUMN THAT USUALLY HAVE HIGH CORELLATION

def is_unique(s):                           #   This runs in O(n) compared to O(n log n) nunique() method
    a = s.to_numpy() 
    return (a[0] == a).all()

def get_high_corr_cols(df:pd.DataFrame, threshold):
    cols = []
    df_col = df.columns
    c = {i:[] for i in df_col}
    corr = df.corr().abs().to_numpy()
    for i,corr_i in enumerate(corr):
        for j, corr_i_j in enumerate(corr_i):
            if(corr_i_j > threshold and i!=j):
                c[df_col[i]].append(df_col[j])
    for i in c:
        if(i not in cols and c[i]!=[]):
            cols.extend(c[i])
    return cols


def corellation_statistic():
    dfs = []
    single_value_cols = []
    data_path = 'datasets\CIC IoT 2023\\'
    for i in range(20):
        file_no = random.randrange(0,169)
        train_file = f'part-{file_no:05d}-363d1ba3-8ab5-4f96-bc25-4d5862db7cb9-c000.csv'
        temp = pd.read_csv(data_path+train_file)
        print(data_path+train_file)
        dfs.append(temp)
    

    # Concatenate all data into one DataFrame
    df = pd.concat(dfs, ignore_index=True)

    # Drop single value columns
    for i in df.columns:
        if(is_unique(df[i])):
            single_value_cols.append(i)
    df.drop(single_value_cols,axis=1, inplace=True) 
    print()

    return get_high_corr_cols(df.iloc[:,:-1],0.95)



corellation = {}


for i in range(100):
    high_corr = corellation_statistic()
    for attr in high_corr:
        try:
            corellation[attr] += 1
        except:
            corellation.update({attr:0}) 

print(sorted(corellation.items(), key=lambda x:x[1]))