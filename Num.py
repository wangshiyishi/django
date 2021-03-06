import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print b
array ([5,6,7,8])#一维数组

print c
array([[1,2,3,4]
      [4,5,6,7]
      [7,8,9,10]])#二维数组
print  a.shape#数组的大小可以通过其shape属性
(4,)
print  c.shape
(3,4)
c.shape = 4,3
c
array([[1,2,3]
       [4,4,5]
       [6,7,7]
       [8,9,10]])#改变每个轴的大小，数组元素在内存中的位置并没有改变：
c.shape = 2,-1
array([[1,2,3,4,5]
       [6,7,8,9,10]])#当某个轴的元素为-1时，将根据数组元素的个数自动计算此轴的长度，因此下面的程序将数组c的shape改为了(2,6)

d = a.reshape((2,2))#使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变
d
array([[1,2]
       [3,4]])
a
array([1,2,3,4])

a[1] = 100
d
array([[1,100]
       [3,4]])

 np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.float)
array([[  1.,   2.,   3.,   4.],
       [  4.,   5.,   6.,   7.],
       [  7.,   8.,   9.,  10.]])

 np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.complex)
array([[  1.+0.j,   2.+0.j,   3.+0.j,   4.+0.j],
       [  4.+0.j,   5.+0.j,   6.+0.j,   7.+0.j],
       [  7.+0.j,   8.+0.j,   9.+0.j,  10.+0.j]])

 a = np.arange(0,12)
 a.shape = 3,4
 a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
a.tofile("a.bin")
 b = np.fromfile("a.bin", dtype=np.float) # 按照float类型读入数据
 b # 读入的数据是错误的
array([  2.12199579e-314,   6.36598737e-314,   1.06099790e-313,
         1.48539705e-313,   1.90979621e-313,   2.33419537e-313])
 a.dtype # 查看a的dtype
dtype('int32')
b = np.fromfile("a.bin", dtype=np.int32) # 按照int32类型读入数据
 b # 数据是一维的
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
 b.shape = 3, 4 # 按照a的shape修改b的shape
 b # 这次终于正确了
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

