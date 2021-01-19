import numpy as np
import pandas as pd
import io
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn import datasets

temp = 'challenge.csv'
df = pd.read_csv(temp,nrows=10000)
ips = df.src_ip.unique()
ports = df.dst_port.unique()
final = {}
for i in ips:
    temp = {}
    temp_df = df.loc[df['src_ip'] == i]
    for j in ports:
        temp_df2 = temp_df.loc[df['dst_port'] == j]
        temp[j] = temp_df2.size
    final[i] = temp

df_to_test = pd.DataFrame.from_dict(final, orient='index')


print(1)