import numpy as np

array_a = np.array([1,2,3,4,5])
print(array_a.shape)

array_b = np.array([[1,2,3,4,5], [1,2,3,4,5]])
print(array_b.shape)

array_c = np.array([[1,2], [3,4], [5,6], [7,8], [9,10]])
print(array_c)

array_d = np.array([[1,2], [3,4]])
print(array_d)
print(array_d.sum())
array = array_d.T
print(array_d + array)
print(np.dot(array_b[:,1], array_b[:,2]))

array2 = np.array([[1,2,3], [2,4,6], [3,6,9]])
print(np.linalg.matrix_rank(array2))
'''
print(array_d.shape)
print(array_d.size)
array_e = array_d.T
print(array_e)
print(array_e[0,1])
print(array_e[:, -2])

array_f = np.zeros((3,3))
print(array_f)
array_f = np.random.random((3,4))
print(array_f)
print(array_f[:,2:4:2])
print(array_f)
greater_than_five_over_ten = array_f > 0.5
print(array_f[greater_than_five_over_ten])

drop_under_five = np.where(array_f > 0.5, array_f, 0)
print(drop_under_five)
'''

print(np.dot(array_a.transpose(), array_b[1,:].transpose()))