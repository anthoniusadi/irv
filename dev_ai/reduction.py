from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def transform(df,features,componen=2):
    
    # features = ['mean','max','std','variance','peak_to_peek']
    x = df.loc[:, features[:-1]].values
    x = StandardScaler().fit_transform(x)

    pca = PCA(n_components=componen)
    principalComponents = pca.fit_transform(x)
    
    if componen==2:
        corpus = pd.DataFrame(data=principalComponents,columns=['pc_1','pc_2'])
        principalDf = pd.DataFrame(data = principalComponents, columns = ['pc_1', 'pc_2'])
        
        corpus['fname']=df['fname']
        # print(corpus)
        corpus.to_csv('./data/csv/corpus_2component_features_acc_2022_12_4.csv')
        
        principalDf.to_csv('./data/csv/2component_features_acc_2022_12_4.csv')
        fig = plt.figure(figsize = (8,8))
        ax = fig.add_subplot(1,1,1) 
        ax.set_xlabel('principal component 1', fontsize = 15)
        ax.set_ylabel('principal component 2', fontsize = 15)
        ax.set_title('2 component PCA', fontsize = 20)
    
        ax.scatter(principalDf['pc_1'], principalDf['pc_2'],c='blue',s=50)
        ax.grid()
        plt.show()
        return principalDf
    else:
        principalDf = pd.DataFrame(data = principalComponents, columns = ['pc_1', 'pc_2','pc_3'])
        print(principalDf)
        y=principalDf.columns
        principalDf.to_csv('./data/csv/3component_features_acc_2022_12_4.csv')
        Xax = principalComponents[:,0]
        Yax = principalComponents[:,1]
        Zax = principalComponents[:,2]
        
        cdict = {0:'red',1:'green'}
        labl = {0:'Malignant',1:'Benign'}
        marker = {0:'*',1:'o'}
        alpha = {0:.3, 1:.5}
        fig = plt.figure(figsize=(7,5))
        ax = fig.add_subplot(111, projection='3d')

        fig.patch.set_facecolor('white')

        # for l in np.unique(y):
        #     ix=np.where(y==l)
        ax.scatter(principalDf['pc_1'], principalDf['pc_2'],principalDf['pc_3'],c='blue',s=50)
        # for loop ends
        ax.set_xlabel("First Principal Component", fontsize=14)
        ax.set_ylabel("Second Principal Component", fontsize=14)
        ax.set_zlabel("Third Principal Component", fontsize=14)

        ax.legend()
        plt.show()

            
    
    
    
# df = pd.read_csv('./data/csv/3component_features_acc_2022_11_16.csv')
# transform(df)
