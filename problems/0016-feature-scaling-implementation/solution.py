import numpy as np

def feature_scaling(data):
    data = data.astype(float)
    std_data = np.round((data - np.mean(data, axis=0)) / np.where(np.std(data, axis=0)==0, 1, np.std(data, axis=0)), 4)
    norm_data = np.round((data - np.min(data, axis=0)) / np.where((np.max(data, axis=0)-np.min(data, axis=0))==0, 1, (np.max(data, axis=0)-np.min(data, axis=0))), 4)
    return std_data.tolist(), norm_data.tolist()