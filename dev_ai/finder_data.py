
import pandas as pd
def find(pc1,pc2):
    df = pd.read_csv('./data/csv/corpus_2component_features_acc_2022_12_4.csv')
    files =df.loc[(df['pc_1'] >= pc1) | (df['pc_2'] <= pc2)]
    print(files)
    print(files.index)
    
find(12, -6)
