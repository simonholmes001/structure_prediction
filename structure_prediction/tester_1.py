import os
import pickle
import numpy as np
import pandas as pd

with open('../output/9atc_feature.pickle', 'rb') as labels_file:
    psi_df = pd.read_pickle(labels_file)
    psi_array = np.array(psi_df)

print(psi_array)
print(psi_array.shape)
