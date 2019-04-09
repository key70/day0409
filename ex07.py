from sklearn import preprocessing
import numpy as np


#문자를 이진화 배열로 만들어 봐요
#           ==> LabelBinarizer


# x = ['yes', 'no', 'yes']
# lb = preprocessing.LabelBinarizer()
# bn = lb.fit_transform(x)
# print(bn)

# x = ['yes', 'no', 'yes', 'cancel']
# lb = preprocessing.LabelBinarizer()
# bn = lb.fit_transform(x)
# print(bn)
#
# r =  np.array([[0, 0, 1]])
# s  = lb.inverse_transform(r)
# print(s)

# help(preprocessing.LabelBinarizer.inverse_transform)



x = ['paris', 'tokyo', 'london', 'paris']
lb = preprocessing.LabelBinarizer()
b = lb.fit_transform(x)
print(b)

r = np.array([[1, 0, 0]])

result = lb.inverse_transform(r)
print(result)
















