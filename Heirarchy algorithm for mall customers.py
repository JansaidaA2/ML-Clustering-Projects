# ------------------------- Heirachical algorithm ----------------------- #

# importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing dataset 

dataset=pd.read_csv(r"C:\Users\Jan Saida\OneDrive\Documents\Desktop\Excel sheets\Mall_Customers.csv")
x=dataset.iloc[:,[3,4]].values

# using scipy library

import scipy.cluster.hierarchy as sch

dendrogram=sch.dendrogram(sch.linkage(x,method='ward'))


from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,metric='euclidean',linkage='ward')
y_hc=hc.fit_predict(x)

plt.scatter(x[y_hc == 0, 0], x[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[y_hc == 1, 0], x[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(x[y_hc == 2, 0], x[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(x[y_hc == 3, 0], x[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(x[y_hc == 4, 0], x[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

y_hc=hc.labels_
dataset['heirachy cluster']=y_hc

dataset.to_csv('heirarchy prediction.csv',index=False)

import os
os.getcwd()
