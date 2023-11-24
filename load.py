

import numpy as np

data = np.load('labels.npy')

print("Original data:")
print(data)


data[1] = 'stoicism'

np.save('labels.npy', data)

data = np.load('labels.npy')

# Print the modified data
print("Modified data:")
print(data)
