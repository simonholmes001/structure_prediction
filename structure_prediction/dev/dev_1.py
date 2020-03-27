import os

import numpy as np
import torch
import pickle

# array_1 = np.load('../output/final_features/adjacency_matrix_4s3a_adjacency.npy', allow_pickle=True)
# array_2 = np.load('../output/final_features/adjacency_matrix_4s3a_amino_acid_tag.npy', allow_pickle=True)
# array_3 = np.load('../output/final_features/adjacency_matrix_4s3a_features.npy', allow_pickle=True)
# array_4 = array_1[0:5]
# tensor = torch.from_numpy(array_1)
# tensor_2 = torch.from_numpy(array_4)
#
# print(type(tensor_2))
# print(tensor_2.shape)
# print(tensor_2)

with open('../output/pickle/5te1_feature', 'rb') as file:
    dataset = pickle.load(file)

with open('../output/pickle/5te1_label', 'rb') as file:
    dataset_2 = pickle.load(file)

# print(dataset.shape)
# print(dataset_2.shape)
#
# print(dataset_2)

for i in range(0,dataset_2.shape[0]):
    print(i)
    print(dataset_2[i])

print(dataset_2.shape)
