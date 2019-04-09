from sklearn import preprocessing
import numpy as np

# 때에따라 데이터의 범위를 축소시켜야 할 때가 있다.
# 값의 범위가 큰 것보다는 값의 범위가 작은 것이
# 기계학습에 훨씬 효율을 높일 수 있어요.
# 가급적 문자데이터 보다는 숫자 데이터를 학습시키는 것이 더 좋고
# 가급적 숫자의 범위를 이진화 시키는 것이 기계학습에 훨씬 효율성이 높을 수 있어요.

x = [
        [1, -1, 3],
        [2, 0, 0],
        [0, 1, -1]]

# binarizer = preprocessing.Binarizer()
# # print(binarizer)
# # print(type(binarizer))
#
# r  = binarizer.fit(x)
# b =  r.transform(x)
# print(b)

b = preprocessing.Binarizer().fit(x).transform(x)
print(b)

