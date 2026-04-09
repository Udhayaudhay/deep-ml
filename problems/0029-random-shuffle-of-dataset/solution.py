import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)
    
    # Generate a range of indices from 0 to the number of samples
    idx = np.arange(X.shape[0])
    
    # Shuffle the indices in-place
    np.random.shuffle(idx)
    
    # Return both arrays indexed by the same shuffled order
    return X[idx], y[idx]