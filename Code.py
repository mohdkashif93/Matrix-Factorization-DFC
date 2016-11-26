
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd


# In[3]:

n_items = 106871
arr = np.arange(n_items)
np.random.shuffle(arr)

orig_splits = []
for x in range(0,11):
    orig_splits.append(arr[x*971:(x+1)*971])

    
cluster = {}
for x in range(0,11):
    for i in orig_splits[x]:
        cluster[i]=x
print cluster


# In[13]:

dataframe1 = pd.read_csv('r1.train', sep='::', names=['user_id', 'item_id', 'rating', 'timestamp'])


# In[16]:

for row in dataframe1.itertuples():
    fileID = str(cluster[row[2]-1])
    f =open("train_"+fileID+".csv","a+")
    f.write(str(row))
    f.close()


# In[17]:

#Conquer Step
C_hat=np.asarray(C_hat)
X_U = C_hat[0][0]
print X_U.shape

X_V = []
X_V.append(C_hat[0][1])
const = np.asarray(C_hat[0][1]).dot(np.linalg.pinv(np.asarray(C_hat[0][1])))
print const.shape
flag = False
for part in C_hat:
    #print part[1].shape
    if flag == False:
        flag = True
        continue
    else:
        temp = const.dot(np.asarray(part[1]))
        temp = np.asarray(temp)
        #print temp.shape
        #print "temp shape"
        X_V.append(temp)
        
X_V = np.asarray(X_V)
print X_V.shape
X_V_final =np.asarray(C_hat[0][1])
flag = False
for x in X_V:
    if flag == False:
        flag = True
        continue
    #print "shapes are"
    #print X_V_final.shape
    #print x.shape
    X_V_final = np.hstack((X_V_final,x))
print X_V_final.shape
print X_U.shape


# In[ ]:



