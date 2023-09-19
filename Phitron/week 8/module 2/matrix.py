import numpy as np

one_d = np.array([1, 3, 4, 54, 6, 67])
two_d = np.array([[1, 3], [3, 5], [7, 9]])
tree_d = np.array([
    [[1, 5, 3], [3, 5, 5], [7, 6, 9]],
    [[1, 5, 3], [3, 5, 5], [7, 6, 9]],
    [[1, 5, 3], [3, 5, 5], [7, 6, 9]]
])

shaped = one_d.reshape(3, 2)
changed = np.flip(shaped)
add = two_d * changed
back_to_one = add.flatten()


# print(back_to_one.dtype)

diff_type = back_to_one.astype('f')

# print(diff_type)
# print(diff_type.dtype)

sorted = np.sort(tree_d)
print(sorted)
